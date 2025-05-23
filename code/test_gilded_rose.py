# -*- coding: utf-8 -*-
import unittest

from gilded_rose import Item, GildedRose


class GildedRoseTest(unittest.TestCase):
    # def test_foo(self):
    #     items = [Item("foo", 0, 0)]
    #     gilded_rose = GildedRose(items)
    #     gilded_rose.update_quality()
    #     self.assertEqual("fixme", items[0].name)

    def test_regular(self):
        items = [
            Item("Regular", 10, 10),
            Item("Regular", 10, 50),
            Item("Regular", 10, 0),
            Item("Regular", 0, 3),
            Item("Regular", -1, 1),
            Item("Regular", 10, 0),
            ]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(gilded_rose.items[0].quality, 9)
        self.assertEqual(gilded_rose.items[0].sell_in, 9)
        self.assertEqual(gilded_rose.items[1].quality, 49)
        self.assertEqual(gilded_rose.items[1].sell_in, 9)
        self.assertEqual(gilded_rose.items[2].quality, 0)
        self.assertEqual(gilded_rose.items[2].sell_in, 9)
        self.assertEqual(gilded_rose.items[3].quality, 1)
        self.assertEqual(gilded_rose.items[3].sell_in, -1)
        self.assertEqual(gilded_rose.items[4].quality, 0)
        self.assertEqual(gilded_rose.items[4].sell_in, -2)
        self.assertEqual(gilded_rose.items[5].quality, 0)
        self.assertEqual(gilded_rose.items[5].sell_in, 9)
    
    def test_conjured(self):
        items = [
            Item("Conjured", 10, 10),
            Item("Conjured", 10, 50),
            Item("Conjured", 10, 0),
            Item("Conjured", 0, 3),
            Item("Conjured", -1, 1),
            Item("Conjured", 10, 0),
            Item("Conjured", -2, 6),
            ]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(gilded_rose.items[0].quality, 8)
        self.assertEqual(gilded_rose.items[0].sell_in, 9)
        self.assertEqual(gilded_rose.items[1].quality, 48)
        self.assertEqual(gilded_rose.items[1].sell_in, 9)
        self.assertEqual(gilded_rose.items[2].quality, 0)
        self.assertEqual(gilded_rose.items[2].sell_in, 9)
        self.assertEqual(gilded_rose.items[3].quality, 0)
        self.assertEqual(gilded_rose.items[3].sell_in, -1)
        self.assertEqual(gilded_rose.items[4].quality, 0)
        self.assertEqual(gilded_rose.items[4].sell_in, -2)
        self.assertEqual(gilded_rose.items[5].quality, 0)
        self.assertEqual(gilded_rose.items[5].sell_in, 9)
        self.assertEqual(gilded_rose.items[6].quality, 2)
        self.assertEqual(gilded_rose.items[6].sell_in, -3)
    
    def test_aged_brie_1(self):
        items = [Item("Aged Brie", 10, 10)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(gilded_rose.items[0].quality, 11)
        self.assertEqual(gilded_rose.items[0].sell_in, 9)

    
    def test_aged_brie_2(self):
        items = [Item("Aged Brie", 1, 10)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(gilded_rose.items[0].quality, 11)
        self.assertEqual(gilded_rose.items[0].sell_in, 0)

    
    def test_aged_brie_3(self):
        items = [Item("Aged Brie", 0, 10)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(gilded_rose.items[0].quality, 12)
        self.assertEqual(gilded_rose.items[0].sell_in, -1)

    
    def test_aged_brie_4(self):
        items = [Item("Aged Brie", -1, 10)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(gilded_rose.items[0].quality, 12)
        self.assertEqual(gilded_rose.items[0].sell_in, -2)

    
    def test_aged_brie_5(self):
        items = [Item("Aged Brie", 10, 50)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(gilded_rose.items[0].quality, 50)
        self.assertEqual(gilded_rose.items[0].sell_in, 9)
    
    def test_sulphuras(self):
        items = [
            Item("Sulfuras, Hand of Ragnaros", 0, 80),
            Item("Sulfuras, Hand of Ragnaros", -1, 80),
            Item("Sulfuras, Hand of Ragnaros", 10, 80),
            ]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(gilded_rose.items[0].quality, 80)
        self.assertEqual(gilded_rose.items[1].quality, 80)
        self.assertEqual(gilded_rose.items[2].quality, 80)
        self.assertEqual(gilded_rose.items[0].sell_in, 0)
        self.assertEqual(gilded_rose.items[1].sell_in, -1)
        self.assertEqual(gilded_rose.items[2].sell_in, 10)
    
    def test_backstage(self):
        items = [
            Item("Backstage passes to a TAFKAL80ETC concert", 0, 40),
            Item("Backstage passes to a TAFKAL80ETC concert", -1, 40),
            Item("Backstage passes to a TAFKAL80ETC concert", 3, 40),
            Item("Backstage passes to a TAFKAL80ETC concert", 8, 40),
            Item("Backstage passes to a TAFKAL80ETC concert", 12, 40),
            Item("Backstage passes to a TAFKAL80ETC concert", 3, 49),
            Item("Backstage passes to a TAFKAL80ETC concert", 8, 49),
            Item("Backstage passes to a TAFKAL80ETC concert", 12, 49),
            ]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(gilded_rose.items[0].quality, 0)
        self.assertEqual(gilded_rose.items[1].quality, 0)
        self.assertEqual(gilded_rose.items[2].quality, 43)
        self.assertEqual(gilded_rose.items[3].quality, 42)
        self.assertEqual(gilded_rose.items[4].quality, 41)
        self.assertEqual(gilded_rose.items[5].quality, 50)
        self.assertEqual(gilded_rose.items[6].quality, 50)
        self.assertEqual(gilded_rose.items[7].quality, 50)


        
if __name__ == '__main__':
    unittest.main()