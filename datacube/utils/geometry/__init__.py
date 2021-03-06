""" Geometric shapes and operations on them
"""

from ._base import (
    Coordinate,
    BoundingBox,
    InvalidCRSError,
    CRS,
    Geometry,
    GeoBox,
    bbox_union,
    bbox_intersection,
    geobox_union_conservative,
    geobox_intersection_conservative,
    intersects,
    scaled_down_geobox,
    point,
    multipoint,
    line,
    mk_point_transformer,
    multiline,
    polygon,
    multipolygon,
    box,
    polygon_from_transform,
    unary_union,
    unary_intersection,
)

from .tools import (
    is_affine_st,
    apply_affine,
    roi_boundary,
    roi_is_empty,
    roi_is_full,
    roi_intersect,
    roi_shape,
    roi_normalise,
    roi_from_points,
    roi_center,
    roi_pad,
    scaled_down_shape,
    scaled_down_roi,
    scaled_up_roi,
    decompose_rws,
    affine_from_pts,
    get_scale_at_point,
    native_pix_transform,
    compute_reproject_roi,
    split_translation,
    compute_axis_overlap,
    w_,
)

from ._warp import (
    warp_affine,
    rio_reproject,
)

__all__ = [
    "Coordinate",
    "BoundingBox",
    "InvalidCRSError",
    "CRS",
    "Geometry",
    "GeoBox",
    "bbox_union",
    "bbox_intersection",
    "geobox_union_conservative",
    "geobox_intersection_conservative",
    "intersects",
    "point",
    "multipoint",
    "line",
    "mk_point_transformer",
    "multiline",
    "polygon",
    "multipolygon",
    "box",
    "polygon_from_transform",
    "unary_union",
    "unary_intersection",
    "is_affine_st",
    "apply_affine",
    "compute_axis_overlap",
    "roi_boundary",
    "roi_is_empty",
    "roi_is_full",
    "roi_intersect",
    "roi_shape",
    "roi_normalise",
    "roi_from_points",
    "roi_center",
    "roi_pad",
    "scaled_down_geobox",
    "scaled_down_shape",
    "scaled_down_roi",
    "scaled_up_roi",
    "decompose_rws",
    "affine_from_pts",
    "get_scale_at_point",
    "native_pix_transform",
    "compute_reproject_roi",
    "split_translation",
    "warp_affine",
    "rio_reproject",
    "w_",
]
