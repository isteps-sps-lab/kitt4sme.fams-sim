from typing import Optional, Any

from fipy.ngsi.entity import BaseEntity as FipyBaseEntity, FloatAttr, TextAttr, Attr, BoolAttr
from pydantic import Field, BaseModel as PydanticBaseModel


class BaseModel(PydanticBaseModel):
    class Config:
        allow_population_by_field_name = True

    def dict(self, *args, **kwargs):
        """
        This method is a workaround to force using aliases as dictionary keys.
        TODO remove it when the option will become available in Fipy.

        :param args:
        :param kwargs:
        :return:
        """
        kwargs['by_alias'] = True
        return super().dict(*args, **kwargs)


class BaseEntity(FipyBaseEntity, BaseModel):
    """
        This class is a workaround to force using aliases as dictionary keys by inheriting our BaseModel.
        TODO remove it when the option will become available in Fipy.
    """
    def __init__(self, **data: Any):
        super().__init__(**data)


class Datetime(BaseModel):
    date_time: str = Field(alias='dateTime')
    format: str
    timezone_id: str = Field(alias='timezoneId')


class Fatigue(BaseModel):
    level: FloatAttr
    timestamp: Datetime


class WorkerStates(BaseModel):
    fatigue: Optional[Fatigue]


class WorkerStatesAttribute(Attr):
    type = "WorkerStatesProperties"
    value: WorkerStates


class WorkerStaticProperties(BaseModel):
    sex: TextAttr
    hiring_date: TextAttr = Field(alias='hiringDate')
    birthday: TextAttr
    weight: FloatAttr
    height: FloatAttr
    smoker: TextAttr
    max_hr: FloatAttr = Field(alias='maxHR')
    waist_circumference: FloatAttr = Field(alias='waistCircumference')
    body_fat: FloatAttr = Field(alias='bodyFat')
    grip_strength_left_avg: FloatAttr = Field(alias='gripStrengthLeftAvg')
    grip_strength_left_std: FloatAttr = Field(alias='gripStrengthLeftStd')
    grip_strength_right_avg: FloatAttr = Field(alias='gripStrengthRightAvg')
    grip_strength_right_std: FloatAttr = Field(alias='gripStrengthRightStd')
    weekly_trainings: FloatAttr = Field(alias='weeklyTrainings')
    training_intensity: TextAttr = Field(alias='trainingIntensity')
    job_experience: TextAttr = Field(alias='jobExperience')
    ompq: FloatAttr = Field(alias='OMPQ')
    is_worker_right_handed: BoolAttr = Field(alias='isWorkerRightHanded')
    household: FloatAttr
    light_work_hour: FloatAttr = Field(alias='lightWorkHour')
    anxiety_past_week: FloatAttr = Field(alias='anxietyPastWeek')
    depressed_past_week: FloatAttr = Field(alias='depressedPastWeek')
    night_sleep: FloatAttr = Field(alias='nightSleep')
    no_work_with_pain: FloatAttr = Field(alias='noWorkWithPain')
    physical_activity_pain: FloatAttr = Field(alias='physicalActivityPain')
    job_satisfaction: FloatAttr = Field(alias='jobSatisfaction')
    heavy_monotonous_work: FloatAttr = Field(alias='heavyMonotonousWork')
    decrease_pain: FloatAttr = Field(alias='decreasePain')
    stop_until_pain_decreases: FloatAttr = Field(alias='stopUntilPainDecreases')


class WorkerStaticPropertiesAttribute(Attr):
    type = "WorkerStaticProperties"
    value: WorkerStaticProperties


class WorkerEntity(BaseEntity):
    type = 'Worker'
    worker_static_properties: Optional[WorkerStaticPropertiesAttribute] = Field(alias='workerStaticProperties')
    worker_states: Optional[WorkerStatesAttribute] = Field(alias='workerStates')
