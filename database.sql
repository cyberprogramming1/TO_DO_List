create database TO_DO_List;

CREATE TABLE Tasks (
    TaskID INT PRIMARY KEY IDENTITY(1,1),
    TaskName NVARCHAR(100),
    Status NVARCHAR(20)
);

select * from Tasks;

delete Tasks;

DBCC CHECKIDENT ('Tasks', RESEED, 0);
