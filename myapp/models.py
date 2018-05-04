# This is where all the application models are stored

# A model is a class that represents tables or
# collections in our database and where every attribute
# of the class is a field of the table or collection

# Each table has an id that is generated automatically.
# This id auto increments

# However, it's better to just create your own PK id since the naming scheme for the auto
# generated one isn't good. (It's just id)

# The Meta class with the db_table attribute allows
# us to name the table (Django automatically names
# the table or collection: myapp_modelName)

from django.db import models


class Students(models.Model):
    student_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    age = models.IntegerField()

    class Meta:
        db_table = "students"

    def __str__(self):
        return self.name
