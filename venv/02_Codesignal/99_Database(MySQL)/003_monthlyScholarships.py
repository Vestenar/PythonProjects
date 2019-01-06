'''
/*Please add ; after each select statement*/
CREATE PROCEDURE monthlyScholarships()
BEGIN
	SELECT id, scholarship/12 "scholarship" FROM scholarships;
END
'''