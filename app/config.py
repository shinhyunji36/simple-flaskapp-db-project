import os

BASE_DIR = os.path.dirname(__file__)

SQLALCHEMY_DATABASE_URI = 'postgresql://jmibzues:qTCQbS5C1MJBFMxmhJruughRAZW2NOHW@rosie.db.elephantsql.com/jmibzues'.format(os.path.join(BASE_DIR, 'workout_diary.db'))
SQLALCHEMY_TRACK_MODIFICATIONS = False