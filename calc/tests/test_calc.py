import unittest
import json
from flask import request, jsonify
from calc import app

app.testing = True

class TestCalc(unittest.TestCase):
    def test_sum1(self):
        tested_app = app.test_client()
        reply = tested_app.get("/calc/sum?m=3&n=5").get_json()
        self.assertEqual(reply["result"], "8")

    def test_sum2(self):
        tested_app = app.test_client()
        reply = tested_app.get("/calc/sum?m=-3&n=5").get_json()
        self.assertEqual(reply["result"], "2")

    def test_div1(self):
        tested_app = app.test_client()
        reply = tested_app.get("/calc/div?m=3&n=0").get_json()
        self.assertEqual(reply["result"], "DivisionByZeroError")

    def test_div2(self):
        tested_app = app.test_client()
        reply = tested_app.get("/calc/div?m=19&n=6").get_json()
        self.assertEqual(reply["result"], "3")

    def test_mul1(self):
        tested_app = app.test_client()
        reply = tested_app.get("/calc/mul?m=3&n=0").get_json()
        self.assertEqual(reply["result"], "0")
    
    def test_mul2(self):
        tested_app = app.test_client()
        reply = tested_app.get("/calc/mul?m=3&n=-4").get_json()
        self.assertEqual(reply["result"], "-12")

    def test_sub1(self):
        tested_app = app.test_client()
        reply = tested_app.get("/calc/sub?m=3&n=5").get_json()
        self.assertEqual(reply["result"], "-2")

    def test_sub2(self):
        tested_app = app.test_client()
        reply = tested_app.get("/calc/sub?m=6&n=3").get_json()
        self.assertEqual(reply["result"], "3")

