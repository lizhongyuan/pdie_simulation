"""
@file feasible.py
@brief Brief description of the file.
@author li.zhong.yuan@outlook.com
@date 2025/2/8
"""

from typing import Any, List

from simulations.PDIE._2Tuple import _2Tuple
from simulations.PDIE._2Tuple_T import _2TupleT
from simulations.PDIE._2Tuple_TS import _2TupleTS
from simulations.PDIE.partial_duration_interval_event_set import PDIES


def remove_unfeasible_elements_of_DI_2tuple_TS(p_2tuple_TS: _2TupleTS,
                                               p_wildcard_unfeasible_2tuple_TS: _2TupleTS) -> _2TupleTS:

    feasible_DI_2tuple_TS: _2TupleTS = _2TupleTS()
    for _2tuple_T in p_2tuple_TS:
        # 1.1 如果在wildcard_unfeasible_2tuple_TS, 则_2tuple_T非法, continue
        if _2tuple_T in p_wildcard_unfeasible_2tuple_TS:
            continue

        # 1.2 如果通配匹配在wildcard_unfeasible_2tuple_TS, 则_2tuple_T非法, continue
        wildcard_matched: bool = False
        for op_ordered_unfeasible_DI_2tuple_T in p_wildcard_unfeasible_2tuple_TS:
            if _2tuple_T.is_wildcard_included(op_ordered_unfeasible_DI_2tuple_T):
                wildcard_matched = True
                break
        if wildcard_matched:
            continue

        # 1.3 合法, 加入到feasible_DI_2tuple_TS
        feasible_DI_2tuple_TS.add(_2tuple_T)

    # 2 ---------- 返回结果 ----------

    return feasible_DI_2tuple_TS


def f_feasible_DI_2tuple_TS(p_PDIE_S: PDIES, p_idx_T: tuple[int,...]) -> _2TupleTS:
    """
    (定义16) Get the feasible subset of the Cartesian product of all members of the DI2TupleSS instance of a finite PDIES instance in index order IdxT
    Args:
        p_PDIE_S (PDIES): A finite PDIES instance
        p_idx_T (tuple[int,...]): An index order

    Returns:
        (_2TupleTS): The feasible subset
    """

    custom_ordered_wildcard_unfeasible_2tuple_TS: _2TupleTS = \
        p_PDIE_S.get_custom_ordered_wildcard_unfeasible_DI_2tuple_TS(p_idx_T)
    custom_ordered_CP_of_DI_2tuple_SS: _2TupleTS = \
        p_PDIE_S.get_custom_ordered_CP_of_DI_2tuple_SS(p_PDIE_S.f_DI_2tuple_SS(), p_idx_T)

    feasible_DI_2tuple_TS: _2TupleTS = \
        remove_unfeasible_elements_of_DI_2tuple_TS(p_2tuple_TS=custom_ordered_CP_of_DI_2tuple_SS,
                                                   p_wildcard_unfeasible_2tuple_TS=custom_ordered_wildcard_unfeasible_2tuple_TS)

    return feasible_DI_2tuple_TS