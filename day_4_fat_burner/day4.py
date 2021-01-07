import os


class BmiCategories:
    """ class for available bmi categories"""
    def get_bmi_categories(self):
        return {
                'Underweight': {
                    'min': 0.0,
                    'max': 18.5,
                    'multiplier': 0.8
                },
                'Normal Range': {
                    'min': 18.5,
                    'max': 25.0,
                    'multiplier': 0.9
                },
                'Overweight—At Risk': {
                    'min': 25,
                    'max': 30,
                    'multiplier': 1.0
                },
                'Overweight—Moderately Obese': {
                    'min': 30,
                    'max': 35,
                    'multiplier': 1.1
                },
                'Overweight—Severely Obese': {
                    'min': 35,
                    'max': 40,
                    'multiplier': 1.2},
                'Overweight - very severely obese': {
                    'min': 40,
                    'max': 100,
                    'multiplier': 1.3}
            }


class PhysicalActivities:
    """ class with available Physical activities"""

    @staticmethod
    def get_activities():
        return ['Walking',
                'Dancing',
                'Swimming',
                'Water aerobics',
                'Jogging and running',
                'Aerobic exercise classes',
                'Bicycle riding(stationary or on a path)']

    @staticmethod
    def avg_training_time():
        return 30.0


class FatBurnerProgram:
    """ class for futburner dedicated """
    def __init__(self, height, weight, time):
        self.height = height
        self.weight = weight
        self.time = time

    def count_bmi(self):
        return round(self.weight/(self.height**2), 2)

    def get_bmi_categories(self):
        bmi = self.count_bmi()
        categories = BmiCategories().get_bmi_categories()
        for key, value in categories.items():
            if value['min'] <= bmi < value['max']:
                return bmi, key, value['multiplier']

    def create_plan(self):
        trainings ={}
        avg_train_time = PhysicalActivities().avg_training_time()
        weekdays = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
        activities = PhysicalActivities.get_activities()
        result = self.get_bmi_categories()
        bmi, key, multiplier = result
        for day in weekdays:
            if avg_train_time * multiplier < self.time:
                trainings[day] = {key: avg_train_time * multiplier for key in activities}
                return trainings
            else:
                trainings[day] = {key: self.time for key in activities}
                return trainings

    def save_plan(self):
        plan = self.create_plan()
        path = os.getcwd()
        with open(os.path.join(path, 'daily.txt'), 'w') as temp_file:
                temp_file.write(str(plan))


def main():
    try:
        weight = float(input("Put your weight:"))
        height = float(input("Put your height in metres [m]:"))
        time = float(input("Please provide your time per day for activity:"))
        FatBurnerProgram(weight, height, time).save_plan()
    except ValueError:
        print("Your input is incorrect")


if __name__ == '__main__':
    main()
