from django.test import TestCase
from .models import Profile, Neighbourhood, Business_centres
from django.contrib.auth.models import User

# Create your tests here.
class Business_centresClass(TestCase):
        # Set up method
    def setUp(self):
        self.testcentre = Business_centres(centre_name="rick", contact_info="070707707", emergency_service=True)

    # Testing  instance
    def test_instance(self):
        self.assertTrue(isinstance(self.testcentre,Business_centres))

    # Testing Save Method
    def test_save_method(self):
        self.testcentre.save_centre()
        testsaved = Business_centres.objects.all()
        self.assertTrue(len(testsaved) > 0)

    # Testing Delete Method
    def test_delete_method(self):
        self.testcentre.save_centre()
        testsaved = Business_centres.objects.all()
        self.assertTrue(len(testsaved) > 0)

        self.testcentre.delete_centre()
        testdelete = Business_centres.objects.filter(centre_name="rick")
        self.assertEqual(len(testdelete), 0)

class NeighbourhoodClass(TestCase):
        # Set up method
    def setUp(self):
        self.testcentre = Business_centres(centre_name="rick", contact_info="070707707", emergency_service=True)
        self.testcentre.save()

        self.testneighbourhood = Neighbourhood(name="Langata")
        self.testneighbourhood.save()
        #add centre with many to many field
        self.testneighbourhood.centres.add(self.testcentre)

    # Testing  instance
    def test_instance(self):
        self.assertTrue(isinstance(self.testneighbourhood,Neighbourhood))

    # Testing Save Method
    def test_save_method(self):
        self.testneighbourhood.save_Neighbourhood()
        testsaved = Neighbourhood.objects.all()
        self.assertTrue(len(testsaved) > 0)

    # Testing Delete Method
    def test_delete_method(self):
        self.testneighbourhood.save_Neighbourhood()
        testsaved = Neighbourhood.objects.all()
        self.assertTrue(len(testsaved) > 0)

        self.testneighbourhood.delete_Neighbourhood()
        testdelete = Neighbourhood.objects.filter(name="Langata")
        self.assertEqual(len(testdelete), 0)

class ProfileClass(TestCase):
        # Set up method
    def setUp(self):
        self.testcentre = Business_centres(centre_name="rick", contact_info="070707707", emergency_service=True)
        self.testcentre.save()

        self.testneighbourhood = Neighbourhood(name="Langata")
        self.testneighbourhood.save()
        #add centre with many to many field
        self.testneighbourhood.centres.add(self.testcentre)

        self.testuser = User(username = "rick101", password="password")
        self.testuser.save()

        self.testprofile = Profile(username=self.testuser, location="Karen", user_avatar="wewweww",neighbourhood=self.testneighbourhood)
        self.testprofile.save()

    # Testing  instance
    def test_instance(self):
        self.assertTrue(isinstance(self.testprofile,Profile))

    # Testing Save Method
    def test_save_method(self):
        self.testprofile.save_profile()
        testsaved = Profile.objects.all()
        self.assertTrue(len(testsaved) > 0)

    # Testing Delete Method
    def test_delete_method(self):
        self.testprofile.save_profile()
        testsaved = Profile.objects.all()
        self.assertTrue(len(testsaved) > 0)

        self.testprofile.delete_profile()
        testdelete = Profile.objects.filter(username=self.testprofile.username)
        self.assertEqual(len(testdelete), 0)
