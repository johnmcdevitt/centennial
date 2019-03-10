from django.db import models

# Create your models here.

# create Floors model
class Floor(models.Model):
    # add attributes/columns
    floorid = models.AutoField(primary_key=True)
    floorlevel = models.SmallIntegerField() # add a validation
    floorname = models.CharField(max_length=20, unique=True)

    # TODO is this needed
    # def get_absolute_url(self):
    #     return reverse('floor_list')

    # ensure users enters valid data- TODO should this be in the form
    def clean(self):
        if self.floorlevel < -5 or self.floorlevel > 100:
            raise models.ValidationError('Floor level should be between -5 to 100')
        return self.floorlevel

    def __str__(self):
        return self.floorname

# create Rooms model
class Room(models.Model):
    roomid = models.AutoField(primary_key=True)
    roomname = models.CharField(max_length=20, unique=True)
    floorname = models.ForeignKey(Floor,on_delete=models.CASCADE,null=True)

    def __str__(self):
        return self.roomname
