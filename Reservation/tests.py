from django.test import TestCase
from .models import Etudiant,Carrel,Creneau,Reservation

# Create your tests here.
class EtudiantTests(TestCase):
    def test_create_etudiant(self):
        etudiant = Etudiant.objects.create_user(email="julientelook@gmail.com")
        self.assertEqual(etudiant.email,"julientelook@gmail.com")
        self.assertEqual(etudiant.hours,20)        
        self.assertTrue(etudiant.is_active)
        self.assertFalse(etudiant.is_staff)
        self.assertFalse(etudiant.is_superuser)


class CarrelTests(TestCase):
    pass



class CreneauTests(TestCase):
    pass



class ReservationTests(TestCase):
    pass






































