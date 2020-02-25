#!/usr/bin/python3
# -*- coding: utf-8 -*-

__all__ = []

import unittest
from argparse import Namespace
from pathlib import Path

from manga_py import img2pdf


class TestCreatePdf(unittest.TestCase):
    kwargs = None
    _output = None
    _pdf_one = None
    _pdf_two = None

    @classmethod
    def setUpClass(cls):
        cls.kwargs = {
            'path': 'tests/images',
            'delete_original_archives': False,
            'delete_original_directories': False,
            'rewrite_exist_pdf': False,
            'dont_include_directories': True,
            'archives_extension': 'zip',
            'output_directory': 'tests/output',
        }

    @classmethod
    def tearDownClass(cls):
        cls._output = cls.kwargs.get('output_directory', 'output')
        cls._pdf_one = Path(cls._output).joinpath('test_directory.pdf')
        cls._pdf_two = Path(cls._output).joinpath('test_archive.pdf')
        cls._pdf_one.is_file() and cls._pdf_one.unlink()
        cls._pdf_two.is_file() and cls._pdf_two.unlink()
        "Hook method for deconstructing the class fixture after running all tests in the class."

    def img2pdf_arguments(self) -> Namespace:
        return Namespace(
            **self.kwargs
        )

    def prepare(self, **kwargs):
        self.kwargs.update(kwargs)
        img2pdf.arguments = self.img2pdf_arguments

    def test_make_pdf(self):
        self.prepare()

        img2pdf.main()

        self.assertGreater(pdf_one.stat().st_size, 1024)
        self.assertGreater(pdf_two.stat().st_size, 1024)

        self.assertAlmostEqual(pdf_one.stat().st_size, pdf_two.stat().st_size, delta=10)
