import os, sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../")))
os.environ['DJANGO_SETTINGS_MODULE'] = 'jdmapi.settings'
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()

from django.db import connection
from accounts.models import *
from locations.models import *
from questions.models import *
from datetime import date, timedelta


class postgres_view():
	"""
	Connects to database
	Create postgres view and queries data within range of dates
	"""
	def __init__(self):
		self.first_day = self.get_first_day(date.today())
		self.last_day =self.get_last_day(date.today())
		self.my_custom_sql()


	def get_first_day(self,dt, d_years=0, d_months=0):
		"""
		Provides first day of month
		"""
	    y, m = dt.year + d_years, dt.month + d_months
	    a, m = divmod(m-1, 12)
	    return date(y+a, m+1, 1)

	def get_last_day(self,dt):
		"""
		Provides last day of month
		"""
	    return self.get_first_day(dt, 0, 1) + timedelta(-1)


	def my_custom_sql(self):
		"""
		Creates postgres view 
		"""	
		cursor = connection.cursor()
		try:
			drop_view = cursor.execute("drop view form1;")
			cursor.execute("""CREATE VIEW form1 AS  select qa.bookmark_id ,qb.visit_id,qb.state_code,qb.district_code, qb.date_visit,
			max(case when question_id=1 then answer  end ) as f1_q1,
			max(case when question_id=2 then answer  end ) as f1_q2,
			max(case when question_id=3 then answer  end ) as f1_q3,
			max(case when question_id=4 then answer  end  ) as f1_q4,
			max(case when question_id=5 then answer  end ) as f1_q5,
			max(case when question_id=6 then answer  end ) as f1_q6,
			max(case when question_id=7 then answer  end ) as f1_q7,
			max(case when question_id=8 then answer  end ) as f1_q8,
			max(case when question_id=9 then answer  end ) as f1_q9
			from questions_bookmark_answers as qa  JOIN questions_bookmark as qb ON  qa.bookmark_id = qb.id 
			where date_visit between %s and %s
			GROUP BY qa.bookmark_id,qb.state_code,qb.district_code,qb.visit_id,qb.date_visit ;""",[self.first_day,self.last_day])
		except Exception as e:
			pass
		
		cursor.execute("select * from form1")
		row = cursor.fetchall()
		print row
		return row

postgres_view()

