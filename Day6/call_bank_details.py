from encapsulation_example import BranchDetails

branch=BranchDetails("ABC123",1000,"Ajay","Kharadi")
branch.deposit(500)
branch.set_branch_name("Hadapsar")
print(branch.get_branch_info())
