from pathlib import Path
from typing import Dict, Union

import numpy as np
import pandas as pd
from PySide2 import QtCore
from tqdm import tqdm

from ..utils import chmod_remove_executable, timer
from .parallel_subtractor import ParallelSubtractor, PoolSubtractor

__all__ = ["ImageProcessQWorker"]


class ImageProcessQWorker(QtCore.QThread):
    process_result = QtCore.Signal(object)
    finished = QtCore.Signal()

    def __init__(
        self,
        parent,
        subtractor: Union[ParallelSubtractor, PoolSubtractor],
        outputdir: Path,
    ) -> "ImageProcessQWorker":
        super().__init__(parent=parent)

        self.subtractors = subtractor
        self.outputfile = Path(outputdir).joinpath("Area.csv")

    def run(self):
        try:
            self.subtractors.start()
            outputarr = np.zeros(
                (
                    self.subtractors.processnum,
                    self.subtractors.roinum,
                ),
                dtype="u4",
            )
            with timer():
                with tqdm(
                    desc=f"[{self.outputfile.parent}]",
                    total=self.subtractors.processnum,
                ) as tbar:
                    count = 0
                    cache: Dict[int, np.ndarray] = {}
                    while True:
                        i, subtmedimg, areadata = self.subtractors.retrieve()
                        if i is None:
                            break
                        cache[i] = subtmedimg
                        outputarr[i] = areadata
                        if count in cache:
                            self.process_result.emit((count, cache.pop(count)))
                            tbar.update()
                            count += 1

                    cache_list = sorted(
                        (item for item in cache.items()), key=lambda item: item[0]
                    )
                    for i, img in cache_list:
                        self.process_result.emit((i, img))
                        tbar.update()
                cache_list = []
                pd.DataFrame(outputarr).to_csv(
                    self.outputfile,
                    index=False,
                    header=["Area"] * self.subtractors.roinum,
                )

                print(f"[SYSTEM] Area.csv was saved at {self.outputfile.parent}")
        except Exception as e:
            pd.DataFrame(outputarr).to_csv(
                self.outputfile,
                index=False,
                header=["Area"] * self.subtractors.roinum,
            )
            print(f"[ERROR] Unfinished Area.csv was saved at {self.outputfile.parent}")
            raise e
        finally:
            cache_list = []
            chmod_remove_executable(self.outputfile)
            self.process_result.emit(None)
            self.finished.emit()
            self.subtractors.kill_workers()
