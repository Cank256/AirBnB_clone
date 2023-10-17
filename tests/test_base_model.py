#!/usr/bin/python3
import unittest
from models.base_model import BaseModel
from datetime import datetime
import os


class TestBaseModel(unittest.TestCase):
    def setUp(self):
        self.base_model = BaseModel()

    def test_attributes(self):
        self.assertTrue(hasattr(self.base_model, "id"))
        self.assertTrue(hasattr(self.base_model, "created_at"))
        self.assertTrue(hasattr(self.base_model, "updated_at"))

    def test_id_generation(self):
        base_model_1 = BaseModel()
        base_model_2 = BaseModel()
        self.assertNotEqual(base_model_1.id, base_model_2.id)

    def test_str_representation(self):
        expected_str = f"[BaseModel] ({self.base_model.id}) \
            {self.base_model.__dict__}"
        self.assertEqual(str(self.base_model), expected_str)

    def test_save_method(self):
        old_updated_at = self.base_model.updated_at
        self.base_model.save()
        new_updated_at = self.base_model.updated_at
        self.assertNotEqual(old_updated_at, new_updated_at)

    def test_to_dict_method(self):
        obj_dict = self.base_model.to_dict()
        self.assertTrue("__class__" in obj_dict)
        self.assertTrue("created_at" in obj_dict)
        self.assertTrue("updated_at" in obj_dict)
        self.assertEqual(obj_dict["__class__"], "BaseModel")
        self.assertEqual(
            obj_dict["created_at"], self.base_model.created_at.isoformat()
        )
        self.assertEqual(
            obj_dict["updated_at"], self.base_model.updated_at.isoformat()
        )

    def test_init_with_dict(self):
        obj_dict = self.base_model.to_dict()
        new_obj = BaseModel(**obj_dict)
        self.assertNotEqual(self.base_model.id, new_obj.id)
        self.assertEqual(self.base_model.created_at, new_obj.created_at)
        self.assertEqual(self.base_model.updated_at, new_obj.updated_at)


if __name__ == '__main__':
    unittest.main()
