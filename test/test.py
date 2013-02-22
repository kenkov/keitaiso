#! /usr/bin/env python
# coding:utf-8

from __future__ import division, print_function
from unittest import TestCase
from keitaiso import Keitaiso


class KeitaisoTest(TestCase):

    def test_keitaiso(self):

        k = Keitaiso(u'動く\t動詞,自立,*,*,五段・カ行イ音便,基本形,動く,ウゴク,ウゴク')
        self.assertEqual(k.chasen_data,
                         u'動く\t動詞,自立,*,*,五段・カ行イ音便,基本形,動く,ウゴク,ウゴク')
        self.assertEqual(k.hyousoukei, u'動く')
        self.assertEqual(k.hinsi, u'動詞')
        self.assertEqual(k.hinsi1, u'自立')
        self.assertEqual(k.hinsi2, u'*')
        self.assertEqual(k.hinsi3, u'*')
        self.assertEqual(k.katuyoukei, u'五段・カ行イ音便')
        self.assertEqual(k.katuyougata, u'基本形')
        self.assertEqual(k.genkei, u'動く')
        self.assertEqual(k.yomi, u'ウゴク')
        self.assertEqual(k.hatuon, u'ウゴク')

        l = Keitaiso(u'1000\t名詞,数,*,*,*,*,*')
        self.assertEqual(l.chasen_data, u'1000\t名詞,数,*,*,*,*,*')
        self.assertEqual(l.hyousoukei, u'1000')
        self.assertEqual(l.hinsi, u'名詞')
        self.assertEqual(l.hinsi1, u'数')
        self.assertEqual(l.hinsi2, u'*')
        self.assertEqual(l.hinsi3, u'*')
        self.assertEqual(l.katuyoukei, u'*')
        self.assertEqual(l.katuyougata, u'*')
        self.assertEqual(l.genkei, u'*')
        self.assertEqual(l.yomi, u'*')
        self.assertEqual(l.hatuon, u'*')
