from project.services.base_service import BaseService


class SecondaryService(BaseService):
    def __init__(self, name):
        super().__init__(name, 15)

    def details(self):
        robot_names = ' '.join(robot.name for robot in self.robots) if self.robots else 'none'
        return f"{self.name} Secondary Service:\nRobots: {robot_names}"
