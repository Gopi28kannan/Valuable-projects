#access orange hrm  files, in run one time for all

#run orangehrm login process
#test case id 1
import Orangehrm_login
print("login file sucessfully runned")
print("-----------------------------------------------------------------------------------")

#run orangehrm invalid login process
#test case id 2
import Orangehrm_invalid_login
print("invalid file sucessfully runned")
print("-----------------------------------------------------------------------------------")

#run orangehrm add employee and fill personal details process
#test case pim id 1
import Orangehrm_add_employee
print("add employee file sucessfully runned")
print("-----------------------------------------------------------------------------------")

#run orangehrm edit employee process
#test case pim id 2
import Orangehrm_edit_employee
print("edit employee file sucessfully runned")
print("-----------------------------------------------------------------------------------")

#run orangehrm delete employee process
#test case pim id 3
import Orangehrm_delete_employee
print("delete employee file sucessfully runned")
print("-----------------------------------------------------------------------------------")

print("\n\n All files successfully run executed")
