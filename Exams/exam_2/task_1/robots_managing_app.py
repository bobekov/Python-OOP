from project.robots.female_robot import FemaleRobot
from project.robots.male_robot import MaleRobot
from project.services.main_service import MainService
from project.services.secondary_service import SecondaryService


class RobotsManagingApp:
    VALID_TYPE_SERVICE = {"MainService": MainService, "SecondaryService": SecondaryService}
    VALID_TYPE_ROBOTS = {"MaleRobot": MaleRobot, "FemaleRobot": FemaleRobot}

    def __init__(self):
        self.robots = []
        self.services = []

    def add_service(self, service_type: str, name: str):
        if service_type not in self.VALID_TYPE_SERVICE:
            raise Exception("Invalid service type!")
        new_service = self.VALID_TYPE_SERVICE[service_type](name)
        self.services.append(new_service)
        return f"{service_type} is successfully added."

    def add_robot(self, robot_type: str, name: str, kind: str, price: float):
        if robot_type not in self.VALID_TYPE_ROBOTS:
            raise Exception("Invalid robot type!")
        new_robot = self.VALID_TYPE_ROBOTS[robot_type](name, kind, price)
        self.robots.append(new_robot)
        return f"{robot_type} is successfully added."

    def add_robot_to_service(self, robot_name: str, service_name: str):
        robot = self._find_robot(robot_name)
        service = self._find_service(service_name)
        if robot.POSSIBLE_SERVICE != service.__class__.__name__:
            return "Unsuitable service."
        if service.capacity <= len(service.robots):
            raise Exception("Not enough capacity for this robot!")
        service.robots.append(robot)
        self.robots.remove(robot)
        return f"Successfully added {robot_name} to {service_name}."

    def remove_robot_from_service(self, robot_name: str, service_name: str):
        service = self._find_service(service_name)
        robot = [r for r in service.robots if r.name == robot_name]
        if not robot:
            raise Exception("No such robot in this service!")
        robot_obj = robot[0]
        service.robots.remove(robot_obj)
        self.robots.append(robot_obj)
        return f"Successfully removed {robot_name} from {service_name}."

    def feed_all_robots_from_service(self, service_name: str):
        service = self._find_service(service_name)
        robots_fed = len([r.eating() for r in service.robots])
        return f"Robots fed: {robots_fed}."

    def service_price(self, service_name: str):
        service = self._find_service(service_name)
        price_robots = sum([r.price for r in service.robots])
        return f"The value of service {service_name} is {price_robots:.2f}."

    def __str__(self):
        return '\n'.join([s.details() for s in self.services])

    def _find_robot(self, robot_name):
        robot = [r for r in self.robots if r.name == robot_name]
        return robot[0] if robot else None

    def _find_service(self, service_name):
        service = [s for s in self.services if s.name == service_name]
        return service[0] if service else None

















