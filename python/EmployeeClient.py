from __future__ import print_function
import logging

import grpc
import EmployeeService_pb2
import EmployeeService_pb2_grpc

import const

def run():
    with grpc.insecure_channel(const.IP+':'+const.PORT) as channel:
        stub = EmployeeService_pb2_grpc.EmployeeServiceStub(channel)

        # Query an employee's data
        response = stub.GetEmployeeDataFromID(EmployeeService_pb2.EmployeeID(id=101))
        print ('Employee\'s data: ' + str(response))

        # Add a new employee
        response = stub.CreateEmployee(EmployeeService_pb2.EmployeeData(id=301, name='Jose da Silva', title='Programmer'))
        print ('Added new employee ' + response.status)

        # Change an employee's title
        response = stub.UpdateEmployeeTitle(EmployeeService_pb2.EmployeeTitleUpdate(id=301, title='Senior Programmer'))
        print ('Updated employee ' + response.status)

        # Delete an employee
        response = stub.DeleteEmployee(EmployeeService_pb2.EmployeeID(id=201))
        print ('Deleted employee ' + response.status)

        # List all employees
        response = stub.ListAllEmployees(EmployeeService_pb2.EmptyMessage())
        print ('All employees: ' + str(response))

        #New Endpoints:

        #New Endpoint 1 - Get Employees Number
        response = stub.GetEmployeeNumber(EmployeeService_pb2.EmptyMessage())
        print ('Employees Number: ' + str(response))

        #New Endpoint 2 - Update Employee salary by Percentage
        response = stub.UpdateEmployeeSalary(EmployeeService_pb2.EmployeeSalaryUpdate(id=301, percentage=0.1))
        print ('Updated employee ' + response.status)

        #New Endpoint 3 - Get All Employees by Salary
        response = stub.GetAllEmployeesBySalary(EmployeeService_pb2.EmployeeSalary(salary=10000))
        print ('All employees: ' + str(response) + " earn more than 10000")

        #New Endpoint 4 - Get All Employees by Title
        response = stub.GetAllEmployeesByTitle(EmployeeService_pb2.EmployeeTitle(title='Programmer'))
        print ('All employees: ' + str(response) + " are programmers")

        #New Endpoint 5 - Increase all employees salary by percentage
        response = stub.IncreaseAllEmployeesSalary(EmployeeService_pb2.EmployeeSalary(salary=0.1))
        print ('All employees salary increased by 10%')

if __name__ == '__main__':
    logging.basicConfig()
    run()