import random
from datetime import datetime, timezone, date

from fipy.sim.sampler import DevicePoolSampler

from famssim.ngsy import *


class WorkerSampler(DevicePoolSampler):

    def new_device_entity(self) -> WorkerEntity:
        return WorkerEntity(
            id='urn:ngsi-ld:Worker:1',
            worker_states=WorkerStatesAttribute.new(
                WorkerStates(
                    fatigue=Fatigue(
                        level=FloatAttr.new(random.randint(0, 10)),
                        timestamp=Datetime(
                            date_time=datetime.now(timezone.utc).isoformat().replace('+00:00', 'Z'),
                            format="ISO",
                            timezone_id="UTC"
                        )
                    )
                )
            ),
            worker_static_properties=WorkerStaticPropertiesAttribute.new(
                WorkerStaticProperties(
                    sex=TextAttr.new(random.choice(['Female', 'Male'])),
                    birthday=TextAttr.new(datetime.strftime(date(random.randint(1970, 1990),
                                                                 random.randint(1, 12),
                                                                 random.randint(1, 28)), "%Y-%m-%d")),
                    hiring_date=TextAttr.new(datetime.strftime(date(random.randint(2005, 2023),
                                                                    random.randint(1, 12),
                                                                    random.randint(1, 28)), "%Y-%m-%d")),
                    weight=FloatAttr.new(random.normalvariate(80, 15)),
                    height=FloatAttr.new(random.normalvariate(180, 20)),
                    max_hr=FloatAttr.new(random.normalvariate(180, 3)),
                    waist_circumference=FloatAttr.new(random.normalvariate(80, 10)),
                    body_fat=FloatAttr.new(random.normalvariate(5, 2)),
                    grip_strength_left_avg=FloatAttr.new(random.normalvariate(44.3, 5)),
                    grip_strength_left_std=FloatAttr.new(random.normalvariate(1, 0.5)),
                    grip_strength_right_avg=FloatAttr.new(random.normalvariate(40.7, 5)),
                    grip_strength_right_std=FloatAttr.new(random.normalvariate(1, 0.5)),
                    smoker=TextAttr.new(random.choice(['Yes', 'No'])),
                    weekly_trainings=FloatAttr.new(random.randint(0, 3)),
                    training_intensity=TextAttr.new(
                        random.choice(['None', 'Low', 'Medium', 'High'])),
                    job_experience=TextAttr.new(
                        random.choice(['None', 'Low', 'Medium', 'High'])),
                    ompq=FloatAttr.new(random.normalvariate(50, 5)),
                    is_worker_right_handed=BoolAttr.new(random.choice([True, False])),
                    household=FloatAttr.new(random.randint(0, 10)),
                    light_work_hour=FloatAttr.new(random.randint(0, 10)),
                    anxiety_past_week=FloatAttr.new(random.randint(0, 10)),
                    depressed_past_week=FloatAttr.new(random.randint(0, 10)),
                    night_sleep=FloatAttr.new(random.randint(0, 10)),
                    no_work_with_pain=FloatAttr.new(random.randint(0, 10)),
                    physical_activity_pain=FloatAttr.new(random.randint(0, 10)),
                    job_satisfaction=FloatAttr.new(random.randint(0, 10)),
                    heavy_monotonous_work=FloatAttr.new(random.randint(0, 10)),
                    decrease_pain=FloatAttr.new(random.randint(0, 10)),
                    stop_until_pain_decreases=FloatAttr.new(random.randint(0, 10)),
                )
            ),
            metadata={}  # if None, an exception occurs
        )
