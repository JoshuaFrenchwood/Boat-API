# -*- coding: utf-8 -*-
"""
Created on Sun Apr 26 18:59:46 2020

@author: joshu
"""
import pytest
import BoatApi as api

class TestClass:
    def test_one(self):
        #Test 1 - Create Boat
        result = {'speed':0,'direction':0}
        api.deleteBoat()
        assert api.createBoat() == result
    def test_two(self):
        #Test 2 - Fail to Create Two Boats
        api.createBoat()
        assert api.createBoat()==None
    
    def test_three(self):
        #Test 3 - Delete Boat from Database
        api.createBoat()
        assert api.deleteBoat() == None
    def test_four(self):
        #Test 4 - Fail to Delete Boat, No Trigger
        api.deleteBoat()
        assert api.deleteBoat() == None
    def test_five(self):
        #Test 5 - Update Boat Data
        api.createBoat()
        speed = 10
        direction = 10
        result = api.updateBoat(speed, direction)
        assert result == {'speed':speed, 'direction': direction}
    def test_six(self):
        #Test 6 - Fail to Update Boat, Too High Speed
        api.deleteBoat()
        api.createBoat()
        speed = 800
        direction = 0
        result = api.updateBoat(speed, direction)
        assert result == None
    def test_seven(self):
        #Test 7 - Fail to Update Boat, Too Low Speed
        api.deleteBoat()
        api.createBoat()
        speed = -100
        direction = 0
        result = api.updateBoat(speed, direction)
        assert result == None
        
    def test_eight(self):
        #Test 8 - Fail to Update Boat, Too High Direction
        api.deleteBoat()
        api.createBoat()
        speed = 10
        direction = 200
        result = api.updateBoat(speed, direction)
        assert result == None
        
    def test_nine(self):
        #Test 9 - Fail to Update Boat, Too Low Direction
        api.deleteBoat()
        api.createBoat()
        speed = 10
        direction = -40
        result = api.updateBoat(speed, direction)
        assert result == None
    def test_ten(self):
        #Test 10 - Get Boat Data
        api.deleteBoat()
        api.createBoat()
        result = {'speed':0, 'direction':0}
        assert result == api.getBoat()
    def test_eleven(self):
        #Test 11 - Fail to Get Boat Data, Database is Empty
        api.deleteBoat()
        assert api.getBoat() == None
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        