from django.test import TestCase
from django.utils import timezone
from django.core.exceptions import ValidationError
from django.db.utils import IntegrityError
# from model_mommy import mommy

from house.models import Floor, Room

# test method for floor
class FloorTest(TestCase):

    def test_create_floor(self):
        floor = Floor.objects.create(floorname="my floor",floorlevel=99)
        self.assertTrue(isinstance(floor, Floor))
        self.assertEqual(floor.floorname, floor.__str__())
        self.assertTrue((floor.floorlevel >= -5) and (floor.floorlevel <= 100))


    def test_illegal_floor_levels(self):
        floor101 = Floor.objects.create(floorname="my floor",floorlevel=101)
        with self.assertRaisesMessage(ValidationError, 'Floor level should be between -5 to 100'):
            floor101.clean()

        floorneg6 = Floor.objects.create(floorname="my floor two",floorlevel=-6)
        with self.assertRaisesMessage(ValidationError, 'Floor level should be between -5 to 100'):
            floor101.clean()

        floor0 = Floor.objects.create(floorname="my floor three",floorlevel=0)
        # clean method will cause test to error out if there is an issue here, no assert needed
        floor0.clean()

    def test_duplicate_floor_name(self):
        floor = Floor.objects.create(floorname="my floor",floorlevel=3)

        with self.assertRaisesMessage(IntegrityError, 'duplicate key value violates unique constraint "house_floors_floorname_key"\nDETAIL:  Key (floorname)=(my floor) already exists.\n'):
            floor_dup = Floor.objects.create(floorname="my floor",floorlevel=-3)

class RoomTest(TestCase):

    def test_room_create(self):
        room = Room.objects.create(roomname="my room")
        self.assertTrue(isinstance(room,Room))
        self.assertEqual(room.roomname, room.__str__())
