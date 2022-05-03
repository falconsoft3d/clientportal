from django.db.models import Manager

from store.models import Product, Color, Size


def build_structure(sizes: int, colors: int) -> list:
    return [[None for _ in range(sizes)] for _ in range(colors)]


def place_variants_into_matrix(
        matrix: list,
        variants: Manager,
        colors: list,
        sizes: list
):
    for variant in variants.all():
        x, y = variant.position(colors, sizes)
        matrix[x][y] = variant

    return matrix


def get_sorted_values(cls, queryset):
    return cls.objects.filter(
        id__in=queryset
    ).order_by('sequence').values('id')


def build_matrix(variants: Manager) -> list:
    variant_colors = variants.filter().distinct('color').values('color')
    sorted_colors = get_sorted_values(
        Color,
        variant_colors
    )

    variant_sizes = variants.filter().distinct('size').values('size')
    sorted_sizes = get_sorted_values(
        Size,
        variant_sizes
    )

    matrix = build_structure(sorted_sizes.count(), sorted_colors.count())

    matrix = place_variants_into_matrix(
        matrix,
        variants,
        list(sorted_colors.values_list('id', flat=True)),
        list(sorted_sizes.values_list('id', flat=True))
    )

    return matrix


def build_variant_structure(product: Product) -> list:
    variants = product.variants

    variants_in_size = variants.filter().distinct('size').count() > 1
    variants_in_color = variants.filter().distinct('color').count() > 1

    result = []

    if variants_in_size and variants_in_color:
        result = build_matrix(variants)
    # else:
    #     result = build_array(variants)

    return result
