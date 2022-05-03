from django.test import TestCase

from mixer.backend.django import mixer

from store.services import build_variant_structure


class TestMatrixServices(TestCase):
    def setUp(self) -> None:
        super().setUp()

        red = mixer.blend('store.Color', name='Red', sequence=1)
        green = mixer.blend('store.Color', name='Green', sequence=2)
        blue = mixer.blend('store.Color', name='Blue', sequence=3)

        l = mixer.blend('store.Size', name='L', sequence=1)
        m = mixer.blend('store.Size', name='M', sequence=2)
        s = mixer.blend('store.Size', name='S', sequence=3)

        self.parent_product = mixer.blend('store.Product')
        self.rl = mixer.blend('store.Product', color=red, size=l, stock=10,
                              parent=self.parent_product.id)
        self.bs = mixer.blend('store.Product', color=blue, size=s, stock=100,
                              parent=self.parent_product.id)
        self.gm = mixer.blend('store.Product', color=green, size=m, stock=1000,
                              parent=self.parent_product.id)

    def test_matrix(self):
        """
        If we have the colors red, green and blue and the sizes L, M, S
        the expected matrix should be like
        Position(M, RedLarge) = (0, 0)
        Position(M, GreenMiddle) = (1, 1)
        Position(M, BlueSmall) = (2, 2)
        """
        matrix = build_variant_structure(self.parent_product)

        self.assertEqual(matrix[0][0], self.rl)
        self.assertEqual(matrix[1][1], self.gm)
        self.assertEqual(matrix[2][2], self.bs)
