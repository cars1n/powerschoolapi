from .DataAccess import StandardAccess
import os
from icecream import ic
from dotenv import load_dotenv
from .AccessToken import AccessToken

# Load environment variables from .env file just once
load_dotenv()

base_url = os.environ.get('POWERSCHOOL_SERVER_URL')
token_instance = AccessToken()
access_token = token_instance.get_access_token()
json_headers = {"Accept": "application/JSON"}

class PS:

    def __init__(self):
        self.standard_access = StandardAccess(access_token, base_url=base_url)

    #Student info
    def get_student_count(self, school_id):
        endpoint = f"ws/v1/school/{school_id}/student/count"
        response = self.standard_access.fetch_data(endpoint, headers=json_headers)
        return response.get('resource', {}).get('count', 0)

    def get_students(self, school_id, pagesize=100):
        total_count = self.get_student_count(school_id)
        total_pages = -(-total_count // pagesize)  # Ceiling division to get total pages

        all_students = []
        for page in range(1, total_pages + 1):
            endpoint = f"ws/v1/school/{school_id}/student"
            params = {'page': page, 'pagesize': pagesize}
            response = self.standard_access.fetch_data(endpoint, params=params, headers=json_headers)

            # Extracting the list of students from the response
            page_students = response.get('students', {}).get('student', [])
            all_students.extend(page_students)

        return all_students

    def get_student(self, student_id):
        endpoint = f"ws/v1/student/{student_id}?expansions=school_enrollment"
        response = self.standard_access.fetch_data(endpoint, headers=json_headers)
        return response.get('student', {})

    def get_student_mom(self, student_id):
        endpoint = f"ws/v1/{student_id}/student/contact/mother"
        return self.standard_access.fetch_data(endpoint, headers=json_headers)

    #def add_student(self, student_data):
    #    endpoint = "ws/v1/student"
    #    student_data['action'] = 'INSERT'
    #    response = self.standard_access.post_data(endpoint, data=student_data, headers=json_headers)
    #    return response

    #def update_student(self, student_id, updated_data):
    #    endpoint = f"ws/v1/student/{student_id}"
    #    updated_data['action'] = 'UPDATE'
    #    response = self.standard_access.put_data(endpoint, data=updated_data, headers=json_headers)
    #    return response

    #District info
    def get_schools(self):
        endpoint = "/ws/v1/district/school"
        response = self.standard_access.fetch_data(endpoint, headers=json_headers)
        return response.get('schools', {}).get('school', [])

    def get_school_count(self):
        endpoint = "/ws/v1/district/school/count"
        response = self.standard_access.fetch_data(endpoint, headers=json_headers)
        return response.get('resource', {}).get('count', 0)

    def get_district_students_count(self):
        endpoint = "/ws/v1/district/student/count"
        response = self.standard_access.fetch_data(endpoint, headers=json_headers)
        return response.get('resource', {}).get('count', 0)

    def get_district_students(self, pagesize=100):
        total_count = self.get_student_count()
        total_pages = -(-total_count // pagesize)

        all_students = []
        for page in range(1, total_pages + 1):
            endpoint = "/ws/v1/district/student"
            params = {'page': page, 'pagesize': pagesize}
            response = self.standard_access.fetch_data(endpoint, params=params, headers=json_headers)

            # Extracting the list of students from the response
            page_students = response.get('students', {}).get('student', [])
            all_students.extend(page_students)

        return all_students

    #School info
    def get_course_count(self, school_id):
        endpoint = f"ws/v1/school/{school_id}/course/count"
        response = self.standard_access.fetch_data(endpoint, headers=json_headers)
        return response.get('resource', {}).get('count', 0)

    def get_staff_count(self, school_id):
        endpoint = f"ws/v1/school/{school_id}/staff/count"
        response = self.standard_access.fetch_data(endpoint, headers=json_headers)
        return response.get('resource', {}).get('count', 0)

    def get_all_staff(self, school_id, pagesize=100):
        total_count = self.get_staff_count(school_id)
        total_pages = -(-total_count // pagesize)

        all_staff = []
        for page in range(1, total_pages + 1):
            endpoint = f"ws/v1/school/{school_id}/staff"
            params = {'page': page, 'pagesize': pagesize}
            response = self.standard_access.fetch_data(endpoint, params=params, headers=json_headers)

            # Extracting the list of staff from the response
            page_staff = response.get('staffs', {}).get('staff', [])
            all_staff.extend(page_staff)

        return all_staff

    def get_terms(self, school_id):
        endpoint = f"ws/v1/school/{school_id}/term"
        response = self.standard_access.fetch_data(endpoint, headers=json_headers)
        return response.get('terms', {}).get('term', [])

    def get_staff(self, staff_id):
        endpoint = f"ws/v1/staff/{staff_id}"
        return self.standard_access.fetch_data(endpoint, headers=json_headers)
