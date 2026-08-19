from django.test import TestCase
from .models import Carrel,Creneau,Reservation
from django.utils import timezone
from accounts.models import CustomUser

# Create your tests here.
class EtudiantTests(TestCase):
    def test_create_etudiant(self):
        etudiant = CustomUser.objects.create_user(email="julientelook@gmail.com")
        self.assertEqual(etudiant.email,"julientelook@gmail.com")
        self.assertEqual(etudiant.hours,20)        
        self.assertTrue(etudiant.is_active) # pas nécessaire
        self.assertFalse(etudiant.is_staff)
        self.assertFalse(etudiant.is_superuser)



class CarrelTests(TestCase):
    def test_create_carrel(self):
        carrel = Carrel.objects.create(numero=101, etage=1, nb_places=2)
        self.assertIsNotNone(carrel.id)
        self.assertEqual(carrel.numero, 101)
        self.assertEqual(carrel.etage, 1)
        self.assertEqual(carrel.nb_places, 2)


class CreneauTests(TestCase):
    def test_create_creneau(self):
        date = timezone.now()
        creneau = Creneau.objects.create(date=date, duration=2)
        self.assertEqual(creneau.date, date)
        self.assertEqual(creneau.duration, 2)


class ReservationTests(TestCase):
    def setUp(self):
        self.etudiant = CustomUser.objects.create_user(email="julientelook@gmail.com")
        self.carrel = Carrel.objects.create(numero=1, etage=1, nb_places=2)
        self.creneau = Creneau.objects.create(date=timezone.now(), duration=1)

    def test_create_reservation(self):
        reservation = Reservation.objects.create(
            etudiant=self.etudiant,
            carrel=self.carrel,
            creneau=self.creneau
        )
        self.assertEqual(reservation.etudiant, self.etudiant)
        self.assertEqual(reservation.carrel, self.carrel)
        self.assertEqual(reservation.creneau, self.creneau)

    def test_reservation_cascade_on_etudiant_delete(self):
        Reservation.objects.create(
            etudiant=self.etudiant,
            carrel=self.carrel,
            creneau=self.creneau
        )
        self.etudiant.delete()
        self.assertEqual(Reservation.objects.count(), 0)

    def test_reservation_cascade_on_carrel_delete(self):
        Reservation.objects.create(
            etudiant=self.etudiant,
            carrel=self.carrel,
            creneau=self.creneau
        )
        self.carrel.delete()
        self.assertEqual(Reservation.objects.count(), 0)






































