# Copyright (c) Meta Platforms, Inc. and affiliates.
# SPDX-License-Identifier: LGPL-2.1-or-later

"""
Memory Management
-----------------

The ``drgn.helpers.linux.mm`` module provides helpers for working with the
Linux memory management (MM) subsystem. Only AArch64, s390x, and x86-64 are
currently supported.
"""

import operator
from typing import Iterator, List, Optional, Union, overload

from _drgn import _linux_helper_direct_mapping_offset, _linux_helper_read_vm
from drgn import IntegerLike, Object, Program, cast
from drgn.helpers.common.format import decode_enum_type_flags

__all__ = (
    "PFN_PHYS",
    "PHYS_PFN",
    "PageCompound",
    "PageHead",
    "PageTail",
    "access_process_vm",
    "access_remote_vm",
    "cmdline",
    "compound_head",
    "compound_nr",
    "compound_order",
    "decode_page_flags",
    "environ",
    "for_each_page",
    "page_size",
    "page_to_pfn",
    "page_to_phys",
    "page_to_virt",
    "pfn_to_page",
    "pfn_to_virt",
    "phys_to_page",
    "phys_to_virt",
    "totalram_pages",
    "virt_to_page",
    "virt_to_pfn",
    "virt_to_phys",
    # Generated by scripts/generate_page_flag_getters.py.
    "PageActive",
    "PageChecked",
    "PageDirty",
    "PageDoubleMap",
    "PageError",
    "PageForeign",
    "PageHWPoison",
    "PageHasHWPoisoned",
    "PageIdle",
    "PageIsolated",
    "PageLRU",
    "PageLocked",
    "PageMappedToDisk",
    "PageMlocked",
    "PageOwnerPriv1",
    "PagePinned",
    "PagePrivate",
    "PagePrivate2",
    "PageReadahead",
    "PageReclaim",
    "PageReferenced",
    "PageReported",
    "PageReserved",
    "PageSavePinned",
    "PageSkipKASanPoison",
    "PageSlab",
    "PageSlobFree",
    "PageSwapBacked",
    "PageUncached",
    "PageUnevictable",
    "PageUptodate",
    "PageVmemmapSelfHosted",
    "PageWaiters",
    "PageWorkingset",
    "PageWriteback",
    "PageXenRemapped",
    "PageYoung",
)


def PageActive(page: Object) -> bool:
    """
    Return whether the ``PG_active`` flag is set on a page.

    :param page: ``struct page *``
    """
    try:
        flag = page.prog_["PG_active"]
    except KeyError:
        return False
    return bool(page.flags & (1 << flag))


def PageChecked(page: Object) -> bool:
    """
    Return whether the ``PG_checked`` flag is set on a page.

    :param page: ``struct page *``
    """
    try:
        flag = page.prog_["PG_checked"]
    except KeyError:
        return False
    return bool(page.flags & (1 << flag))


def PageDirty(page: Object) -> bool:
    """
    Return whether the ``PG_dirty`` flag is set on a page.

    :param page: ``struct page *``
    """
    try:
        flag = page.prog_["PG_dirty"]
    except KeyError:
        return False
    return bool(page.flags & (1 << flag))


def PageDoubleMap(page: Object) -> bool:
    """
    Return whether the ``PG_double_map`` flag is set on a page.

    :param page: ``struct page *``
    """
    try:
        flag = page.prog_["PG_double_map"]
    except KeyError:
        return False
    return bool(page.flags & (1 << flag))


def PageError(page: Object) -> bool:
    """
    Return whether the ``PG_error`` flag is set on a page.

    :param page: ``struct page *``
    """
    try:
        flag = page.prog_["PG_error"]
    except KeyError:
        return False
    return bool(page.flags & (1 << flag))


def PageForeign(page: Object) -> bool:
    """
    Return whether the ``PG_foreign`` flag is set on a page.

    :param page: ``struct page *``
    """
    try:
        flag = page.prog_["PG_foreign"]
    except KeyError:
        return False
    return bool(page.flags & (1 << flag))


def PageHWPoison(page: Object) -> bool:
    """
    Return whether the ``PG_hwpoison`` flag is set on a page.

    :param page: ``struct page *``
    """
    try:
        flag = page.prog_["PG_hwpoison"]
    except KeyError:
        return False
    return bool(page.flags & (1 << flag))


def PageHasHWPoisoned(page: Object) -> bool:
    """
    Return whether the ``PG_has_hwpoisoned`` flag is set on a page.

    :param page: ``struct page *``
    """
    try:
        flag = page.prog_["PG_has_hwpoisoned"]
    except KeyError:
        return False
    return bool(page.flags & (1 << flag))


def PageIdle(page: Object) -> bool:
    """
    Return whether the ``PG_idle`` flag is set on a page.

    :param page: ``struct page *``
    """
    try:
        flag = page.prog_["PG_idle"]
    except KeyError:
        return False
    return bool(page.flags & (1 << flag))


def PageIsolated(page: Object) -> bool:
    """
    Return whether the ``PG_isolated`` flag is set on a page.

    :param page: ``struct page *``
    """
    try:
        flag = page.prog_["PG_isolated"]
    except KeyError:
        return False
    return bool(page.flags & (1 << flag))


def PageLRU(page: Object) -> bool:
    """
    Return whether the ``PG_lru`` flag is set on a page.

    :param page: ``struct page *``
    """
    try:
        flag = page.prog_["PG_lru"]
    except KeyError:
        return False
    return bool(page.flags & (1 << flag))


def PageLocked(page: Object) -> bool:
    """
    Return whether the ``PG_locked`` flag is set on a page.

    :param page: ``struct page *``
    """
    try:
        flag = page.prog_["PG_locked"]
    except KeyError:
        return False
    return bool(page.flags & (1 << flag))


def PageMappedToDisk(page: Object) -> bool:
    """
    Return whether the ``PG_mappedtodisk`` flag is set on a page.

    :param page: ``struct page *``
    """
    try:
        flag = page.prog_["PG_mappedtodisk"]
    except KeyError:
        return False
    return bool(page.flags & (1 << flag))


def PageMlocked(page: Object) -> bool:
    """
    Return whether the ``PG_mlocked`` flag is set on a page.

    :param page: ``struct page *``
    """
    try:
        flag = page.prog_["PG_mlocked"]
    except KeyError:
        return False
    return bool(page.flags & (1 << flag))


def PageOwnerPriv1(page: Object) -> bool:
    """
    Return whether the ``PG_owner_priv_1`` flag is set on a page.

    :param page: ``struct page *``
    """
    try:
        flag = page.prog_["PG_owner_priv_1"]
    except KeyError:
        return False
    return bool(page.flags & (1 << flag))


def PagePinned(page: Object) -> bool:
    """
    Return whether the ``PG_pinned`` flag is set on a page.

    :param page: ``struct page *``
    """
    try:
        flag = page.prog_["PG_pinned"]
    except KeyError:
        return False
    return bool(page.flags & (1 << flag))


def PagePrivate(page: Object) -> bool:
    """
    Return whether the ``PG_private`` flag is set on a page.

    :param page: ``struct page *``
    """
    try:
        flag = page.prog_["PG_private"]
    except KeyError:
        return False
    return bool(page.flags & (1 << flag))


def PagePrivate2(page: Object) -> bool:
    """
    Return whether the ``PG_private_2`` flag is set on a page.

    :param page: ``struct page *``
    """
    try:
        flag = page.prog_["PG_private_2"]
    except KeyError:
        return False
    return bool(page.flags & (1 << flag))


def PageReadahead(page: Object) -> bool:
    """
    Return whether the ``PG_readahead`` flag is set on a page.

    :param page: ``struct page *``
    """
    try:
        flag = page.prog_["PG_readahead"]
    except KeyError:
        return False
    return bool(page.flags & (1 << flag))


def PageReclaim(page: Object) -> bool:
    """
    Return whether the ``PG_reclaim`` flag is set on a page.

    :param page: ``struct page *``
    """
    try:
        flag = page.prog_["PG_reclaim"]
    except KeyError:
        return False
    return bool(page.flags & (1 << flag))


def PageReferenced(page: Object) -> bool:
    """
    Return whether the ``PG_referenced`` flag is set on a page.

    :param page: ``struct page *``
    """
    try:
        flag = page.prog_["PG_referenced"]
    except KeyError:
        return False
    return bool(page.flags & (1 << flag))


def PageReported(page: Object) -> bool:
    """
    Return whether the ``PG_reported`` flag is set on a page.

    :param page: ``struct page *``
    """
    try:
        flag = page.prog_["PG_reported"]
    except KeyError:
        return False
    return bool(page.flags & (1 << flag))


def PageReserved(page: Object) -> bool:
    """
    Return whether the ``PG_reserved`` flag is set on a page.

    :param page: ``struct page *``
    """
    try:
        flag = page.prog_["PG_reserved"]
    except KeyError:
        return False
    return bool(page.flags & (1 << flag))


def PageSavePinned(page: Object) -> bool:
    """
    Return whether the ``PG_savepinned`` flag is set on a page.

    :param page: ``struct page *``
    """
    try:
        flag = page.prog_["PG_savepinned"]
    except KeyError:
        return False
    return bool(page.flags & (1 << flag))


def PageSkipKASanPoison(page: Object) -> bool:
    """
    Return whether the ``PG_skip_kasan_poison`` flag is set on a page.

    :param page: ``struct page *``
    """
    try:
        flag = page.prog_["PG_skip_kasan_poison"]
    except KeyError:
        return False
    return bool(page.flags & (1 << flag))


def PageSlab(page: Object) -> bool:
    """
    Return whether the ``PG_slab`` flag is set on a page.

    :param page: ``struct page *``
    """
    try:
        flag = page.prog_["PG_slab"]
    except KeyError:
        return False
    return bool(page.flags & (1 << flag))


def PageSlobFree(page: Object) -> bool:
    """
    Return whether the ``PG_slob_free`` flag is set on a page.

    :param page: ``struct page *``
    """
    try:
        flag = page.prog_["PG_slob_free"]
    except KeyError:
        return False
    return bool(page.flags & (1 << flag))


def PageSwapBacked(page: Object) -> bool:
    """
    Return whether the ``PG_swapbacked`` flag is set on a page.

    :param page: ``struct page *``
    """
    try:
        flag = page.prog_["PG_swapbacked"]
    except KeyError:
        return False
    return bool(page.flags & (1 << flag))


def PageUncached(page: Object) -> bool:
    """
    Return whether the ``PG_uncached`` flag is set on a page.

    :param page: ``struct page *``
    """
    try:
        flag = page.prog_["PG_uncached"]
    except KeyError:
        return False
    return bool(page.flags & (1 << flag))


def PageUnevictable(page: Object) -> bool:
    """
    Return whether the ``PG_unevictable`` flag is set on a page.

    :param page: ``struct page *``
    """
    try:
        flag = page.prog_["PG_unevictable"]
    except KeyError:
        return False
    return bool(page.flags & (1 << flag))


def PageUptodate(page: Object) -> bool:
    """
    Return whether the ``PG_uptodate`` flag is set on a page.

    :param page: ``struct page *``
    """
    try:
        flag = page.prog_["PG_uptodate"]
    except KeyError:
        return False
    return bool(page.flags & (1 << flag))


def PageVmemmapSelfHosted(page: Object) -> bool:
    """
    Return whether the ``PG_vmemmap_self_hosted`` flag is set on a page.

    :param page: ``struct page *``
    """
    try:
        flag = page.prog_["PG_vmemmap_self_hosted"]
    except KeyError:
        return False
    return bool(page.flags & (1 << flag))


def PageWaiters(page: Object) -> bool:
    """
    Return whether the ``PG_waiters`` flag is set on a page.

    :param page: ``struct page *``
    """
    try:
        flag = page.prog_["PG_waiters"]
    except KeyError:
        return False
    return bool(page.flags & (1 << flag))


def PageWorkingset(page: Object) -> bool:
    """
    Return whether the ``PG_workingset`` flag is set on a page.

    :param page: ``struct page *``
    """
    try:
        flag = page.prog_["PG_workingset"]
    except KeyError:
        return False
    return bool(page.flags & (1 << flag))


def PageWriteback(page: Object) -> bool:
    """
    Return whether the ``PG_writeback`` flag is set on a page.

    :param page: ``struct page *``
    """
    try:
        flag = page.prog_["PG_writeback"]
    except KeyError:
        return False
    return bool(page.flags & (1 << flag))


def PageXenRemapped(page: Object) -> bool:
    """
    Return whether the ``PG_xen_remapped`` flag is set on a page.

    :param page: ``struct page *``
    """
    try:
        flag = page.prog_["PG_xen_remapped"]
    except KeyError:
        return False
    return bool(page.flags & (1 << flag))


def PageYoung(page: Object) -> bool:
    """
    Return whether the ``PG_young`` flag is set on a page.

    :param page: ``struct page *``
    """
    try:
        flag = page.prog_["PG_young"]
    except KeyError:
        return False
    return bool(page.flags & (1 << flag))


# End generated by scripts/generate_page_flag_getters.py.


def PageCompound(page: Object) -> bool:
    """
    Return whether a page is part of a `compound page
    <https://lwn.net/Articles/619514/>`_.

    :param page: ``struct page *``
    """
    page = page.read_()
    return bool(
        (page.flags & (1 << page.prog_["PG_head"])) or (page.compound_head.read_() & 1)
    )


# HugeTLB Vmemmap Optimization (HVO) creates "fake" head pages that are
# actually tail pages. See Linux kernel commit e7d324850bfc ("mm: hugetlb: free
# the 2nd vmemmap page associated with each HugeTLB page") (in v5.18) and
# https://www.kernel.org/doc/html/latest/mm/vmemmap_dedup.html.
def _page_is_fake_head(page: Object) -> bool:
    head = page[1].compound_head.value_()
    return bool(head & 1) and (head - 1) != page.value_()


def PageHead(page: Object) -> bool:
    """
    Return whether a page is a head page in a `compound page`_.

    :param page: ``struct page *``
    """
    page = page.read_()
    return bool(
        page.flags & (1 << page.prog_["PG_head"]) and not _page_is_fake_head(page)
    )


def PageTail(page: Object) -> bool:
    """
    Return whether a page is a tail page in a `compound page`_.

    :param page: ``struct page *``
    """
    page = page.read_()
    if page.compound_head.value_() & 1:
        return True
    if page.flags & (1 << page.prog_["PG_head"]):
        return _page_is_fake_head(page)
    return False


def compound_head(page: Object) -> Object:
    """
    Get the head page associated with a page.

    If *page* is a tail page, this returns the head page of the `compound
    page`_ it belongs to. Otherwise, it returns *page*.

    :param page: ``struct page *``
    :return: ``struct page *``
    """
    page = page.read_()
    head = page.compound_head.read_()
    if head & 1:
        return cast(page.type_, head - 1)
    # Handle fake head pages (see _page_is_fake_head()).
    if page.flags & (1 << page.prog_["PG_head"]):
        head = page[1].compound_head.read_()
        if head & 1:
            return cast(page.type_, head - 1)
    return page


def compound_order(page: Object) -> Object:
    """
    Return the allocation order of a potentially `compound page`_.

    :param page: ``struct page *``
    :return: ``unsigned int``
    """
    if not PageHead(page):
        return Object(page.prog_, "unsigned int", 0)
    return cast("unsigned int", page[1].compound_order)


def compound_nr(page: Object) -> Object:
    """
    Return the number of pages in a potentially `compound page`_.

    :param page: ``struct page *``
    :return: ``unsigned long``
    """
    if not PageHead(page):
        return Object(page.prog_, "unsigned long", 1)
    return Object(page.prog_, "unsigned long", 1) << page[1].compound_order


def page_size(page: Object) -> Object:
    """
    Return the number of bytes in a potentially `compound page`_.

    :param page: ``struct page *``
    :return: ``unsigned long``
    """
    return page.prog_["PAGE_SIZE"] << compound_order(page)


def decode_page_flags(page: Object) -> str:
    """
    Get a human-readable representation of the flags set on a page.

    >>> decode_page_flags(page)
    'PG_uptodate|PG_dirty|PG_lru|PG_reclaim|PG_swapbacked|PG_readahead|PG_savepinned|PG_isolated|PG_reported'

    :param page: ``struct page *``
    """
    NR_PAGEFLAGS = page.prog_["__NR_PAGEFLAGS"]
    PAGEFLAGS_MASK = (1 << NR_PAGEFLAGS.value_()) - 1
    return decode_enum_type_flags(
        page.flags.value_() & PAGEFLAGS_MASK, NR_PAGEFLAGS.type_
    )


# Get the struct page * for PFN 0.
def _page0(prog: Program) -> Object:
    try:
        return prog.cache["page0"]
    except KeyError:
        pass
    try:
        # With CONFIG_SPARSEMEM_VMEMMAP=y, page 0 is vmemmap.
        page0 = prog["vmemmap"]
    except KeyError:
        contig_page_data = prog["contig_page_data"]
        # With CONFIG_FLATMEM=y, page 0 is mem_map - ARCH_PFN_OFFSET, but we
        # can't determine ARCH_PFN_OFFSET easily. Alternatively,
        # contig_page_data.node_mem_map is the struct page * for
        # contig_page_data.node_start_pfn, therefore page 0 is:
        page0 = contig_page_data.node_mem_map - contig_page_data.node_start_pfn
    # The struct page array is not contiguous for CONFIG_SPARSEMEM=y with
    # CONFIG_SPARSEMEM_VMEMMAP=n or CONFIG_DISCONTIGMEM=y, so those are not
    # supported yet.
    prog.cache["page0"] = page0
    return page0


def for_each_page(prog: Program) -> Iterator[Object]:
    """
    Iterate over every ``struct page *`` from the minimum to the maximum page.

    .. note::

        This may include offline pages which don't have a valid ``struct
        page``. Wrap accesses in a ``try`` ... ``except``
        :class:`drgn.FaultError`:

        >>> for page in for_each_page(prog):
        ...     try:
        ...         if PageLRU(page):
        ...             print(hex(page))
        ...     except drgn.FaultError:
        ...         continue
        0xfffffb4a000c0000
        0xfffffb4a000c0040
        ...

        This may be fixed in the future.

    :return: Iterator of ``struct page *`` objects.
    """
    page0 = _page0(prog)
    for i in range(prog["min_low_pfn"], prog["max_pfn"]):
        yield page0 + i


@overload
def PFN_PHYS(pfn: Object) -> Object:
    """"""
    ...


@overload
def PFN_PHYS(prog: Program, pfn: IntegerLike) -> Object:
    """
    Get the physical address of a page frame number (PFN).

    The PFN can be given as an :class:`~drgn.Object` or as a
    :class:`~drgn.Program` and an integer.

    :param pfn: ``unsigned long``
    :return: ``phys_addr_t``
    """
    ...


def PFN_PHYS(  # type: ignore  # Need positional-only arguments.
    prog_or_pfn: Union[Program, Object], pfn: Optional[IntegerLike] = None
) -> Object:
    if pfn is None:
        assert isinstance(prog_or_pfn, Object)
        prog = prog_or_pfn.prog_
        pfn = prog_or_pfn
    else:
        assert isinstance(prog_or_pfn, Program)
        prog = prog_or_pfn
    return Object(prog, "phys_addr_t", operator.index(pfn)) << prog["PAGE_SHIFT"]


@overload
def PHYS_PFN(addr: Object) -> Object:
    """"""
    ...


@overload
def PHYS_PFN(prog: Program, addr: int) -> Object:
    """
    Get the page frame number (PFN) of a physical address.

    The address can be given as an :class:`~drgn.Object` or as a
    :class:`~drgn.Program` and an integer.

    :param addr: ``phys_addr_t``
    :return: ``unsigned long``
    """
    ...


def PHYS_PFN(  # type: ignore  # Need positional-only arguments.
    prog_or_addr: Union[Program, Object], addr: Optional[IntegerLike] = None
) -> Object:
    if addr is None:
        assert isinstance(prog_or_addr, Object)
        prog = prog_or_addr.prog_
        addr = prog_or_addr
    else:
        assert isinstance(prog_or_addr, Program)
        prog = prog_or_addr
    return Object(prog, "unsigned long", operator.index(addr)) >> prog["PAGE_SHIFT"]


def page_to_pfn(page: Object) -> Object:
    """
    Get the page frame number (PFN) of a page.

    :param page: ``struct page *``
    :return: ``unsigned long``
    """
    return cast("unsigned long", page - _page0(page.prog_))


def page_to_phys(page: Object) -> Object:
    """
    Get the physical address of a page.

    :param page: ``struct page *``
    :return: ``phys_addr_t``
    """
    return PFN_PHYS(page_to_pfn(page))


def page_to_virt(page: Object) -> Object:
    """
    Get the directly mapped virtual address of a page.

    :param page: ``struct page *``
    :return: ``void *``
    """
    return pfn_to_virt(page_to_pfn(page))


@overload
def pfn_to_page(pfn: Object) -> Object:
    """"""
    ...


@overload
def pfn_to_page(prog: Program, pfn: IntegerLike) -> Object:
    """
    Get the page with a page frame number (PFN).

    The PFN can be given as an :class:`~drgn.Object` or as a
    :class:`~drgn.Program` and an integer.

    :param pfn: ``unsigned long``
    :return: ``struct page *``
    """
    ...


def pfn_to_page(  # type: ignore  # Need positional-only arguments.
    prog_or_pfn: Union[Program, Object], pfn: Optional[IntegerLike] = None
) -> Object:
    if pfn is None:
        assert isinstance(prog_or_pfn, Object)
        prog = prog_or_pfn.prog_
        pfn = prog_or_pfn
    else:
        assert isinstance(prog_or_pfn, Program)
        prog = prog_or_pfn
    return _page0(prog) + pfn


@overload
def pfn_to_virt(pfn: Object) -> Object:
    """"""
    ...


@overload
def pfn_to_virt(prog: Program, pfn: IntegerLike) -> Object:
    """
    Get the directly mapped virtual address of a page frame number (PFN).

    The PFN can be given as an :class:`~drgn.Object` or as a
    :class:`~drgn.Program` and an integer.

    :param pfn: ``unsigned long``
    :return: ``void *``
    """


def pfn_to_virt(  # type: ignore  # Need positional-only arguments.
    prog_or_pfn: Union[Program, Object], pfn: Optional[IntegerLike] = None
) -> Object:
    return phys_to_virt(PFN_PHYS(prog_or_pfn, pfn))  # type: ignore


@overload
def phys_to_page(addr: Object) -> Object:
    """"""
    ...


@overload
def phys_to_page(prog: Program, addr: IntegerLike) -> Object:
    """
    Get the page containing a physical address.

    The address can be given as an :class:`~drgn.Object` or as a
    :class:`~drgn.Program` and an integer.

    :param addr: ``phys_addr_t``
    :return: ``struct page *``
    """
    ...


def phys_to_page(  # type: ignore  # Need positional-only arguments.
    prog_or_addr: Union[Program, Object], addr: Optional[IntegerLike] = None
) -> Object:
    return pfn_to_page(PHYS_PFN(prog_or_addr, addr))  # type: ignore


@overload
def phys_to_virt(addr: Object) -> Object:
    """"""
    ...


@overload
def phys_to_virt(prog: Program, addr: IntegerLike) -> Object:
    """
    Get the directly mapped virtual address of a physical address.

    The address can be given as an :class:`~drgn.Object` or as a
    :class:`~drgn.Program` and an integer.

    :param addr: ``phys_addr_t``
    :return: ``void *``
    """
    ...


def phys_to_virt(  # type: ignore  # Need positional-only arguments.
    prog_or_addr: Union[Program, Object], addr: Optional[IntegerLike] = None
):
    if addr is None:
        assert isinstance(prog_or_addr, Object)
        prog = prog_or_addr.prog_
        addr = prog_or_addr
    else:
        assert isinstance(prog_or_addr, Program)
        prog = prog_or_addr
    return Object(
        prog, "void *", operator.index(addr) + _linux_helper_direct_mapping_offset(prog)
    )


@overload
def virt_to_page(addr: Object) -> Object:
    """"""
    ...


@overload
def virt_to_page(prog: Program, addr: IntegerLike) -> Object:
    """
    Get the page containing a directly mapped virtual address.

    The address can be given as an :class:`~drgn.Object` or as a
    :class:`~drgn.Program` and an integer.

    :param addr: ``void *``
    :return: ``struct page *``
    """
    ...


def virt_to_page(  # type: ignore  # Need positional-only arguments.
    prog_or_addr: Union[Program, Object], addr: Optional[IntegerLike] = None
) -> Object:
    return pfn_to_page(virt_to_pfn(prog_or_addr, addr))  # type: ignore[arg-type]


@overload
def virt_to_pfn(addr: Object) -> Object:
    """"""
    ...


@overload
def virt_to_pfn(prog: Program, addr: IntegerLike) -> Object:
    """
    Get the page frame number (PFN) of a directly mapped virtual address.

    The address can be given as an :class:`~drgn.Object` or as a
    :class:`~drgn.Program` and an integer.

    :param addr: ``void *``
    :return: ``unsigned long``
    """
    ...


def virt_to_pfn(  # type: ignore  # Need positional-only arguments.
    prog_or_addr: Union[Program, Object], addr: Optional[IntegerLike] = None
) -> Object:
    return PHYS_PFN(virt_to_phys(prog_or_addr, addr))  # type: ignore


@overload
def virt_to_phys(addr: Object) -> Object:
    """"""
    ...


@overload
def virt_to_phys(prog: Program, addr: IntegerLike) -> Object:
    """
    Get the physical address of a directly mapped virtual address.

    The address can be given as an :class:`~drgn.Object` or as a
    :class:`~drgn.Program` and an integer.

    :param addr: ``void *``
    :return: ``phys_addr_t``
    """
    ...


def virt_to_phys(  # type: ignore  # Need positional-only arguments.
    prog_or_addr: Union[Program, Object], addr: Optional[IntegerLike] = None
) -> Object:
    if addr is None:
        assert isinstance(prog_or_addr, Object)
        prog = prog_or_addr.prog_
        addr = prog_or_addr
    else:
        assert isinstance(prog_or_addr, Program)
        prog = prog_or_addr
    return Object(
        prog,
        "unsigned long",
        operator.index(addr) - _linux_helper_direct_mapping_offset(prog),
    )


def access_process_vm(task: Object, address: IntegerLike, size: IntegerLike) -> bytes:
    """
    Read memory from a task's virtual address space.

    >>> task = find_task(prog, 1490152)
    >>> access_process_vm(task, 0x7f8a62b56da0, 12)
    b'hello, world'

    :param task: ``struct task_struct *``
    :param address: Starting address.
    :param size: Number of bytes to read.
    """
    return _linux_helper_read_vm(task.prog_, task.mm.pgd, address, size)


def access_remote_vm(mm: Object, address: IntegerLike, size: IntegerLike) -> bytes:
    """
    Read memory from a virtual address space. This is similar to
    :func:`access_process_vm()`, but it takes a ``struct mm_struct *`` instead
    of a ``struct task_struct *``.

    >>> task = find_task(prog, 1490152)
    >>> access_remote_vm(task.mm, 0x7f8a62b56da0, 12)
    b'hello, world'

    :param mm: ``struct mm_struct *``
    :param address: Starting address.
    :param size: Number of bytes to read.
    """
    return _linux_helper_read_vm(mm.prog_, mm.pgd, address, size)


def cmdline(task: Object) -> List[bytes]:
    """
    Get the list of command line arguments of a task.

    >>> cmdline(find_task(prog, 1495216))
    [b'vim', b'drgn/helpers/linux/mm.py']

    .. code-block:: console

        $ tr '\\0' ' ' < /proc/1495216/cmdline
        vim drgn/helpers/linux/mm.py

    :param task: ``struct task_struct *``
    """
    mm = task.mm.read_()
    arg_start = mm.arg_start.value_()
    arg_end = mm.arg_end.value_()
    return access_remote_vm(mm, arg_start, arg_end - arg_start).split(b"\0")[:-1]


def environ(task: Object) -> List[bytes]:
    """
    Get the list of environment variables of a task.

    >>> environ(find_task(prog, 1497797))
    [b'HOME=/root', b'PATH=/usr/local/sbin:/usr/local/bin:/usr/bin', b'LOGNAME=root']

    .. code-block:: console

        $ tr '\\0' '\\n' < /proc/1497797/environ
        HOME=/root
        PATH=/usr/local/sbin:/usr/local/bin:/usr/bin
        LOGNAME=root

    :param task: ``struct task_struct *``
    """
    mm = task.mm.read_()
    env_start = mm.env_start.value_()
    env_end = mm.env_end.value_()
    return access_remote_vm(mm, env_start, env_end - env_start).split(b"\0")[:-1]


def totalram_pages(prog: Program) -> int:
    """
    Return the total number of RAM memory pages.
    """

    try:
        # The variable is present since Linux kernel commit ca79b0c211af63fa32
        # ("mm: convert totalram_pages and totalhigh_pages variables
        # to atomic") (in v5.0).
        return prog["_totalram_pages"].counter.value_()
    except KeyError:
        return prog["totalram_pages"].value_()
