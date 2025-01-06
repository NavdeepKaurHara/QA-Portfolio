
I have used Pytest with Selenium to write these tests. test_assessment.py contains the tests , utils.py has the
helper functions and locators.py has all the locators used in tests. I have created functions for the repetitive
tasks for example all the tests require navigating to the Home Page. So,every test requiring navigation will
call that function. This makes our code readable, reusable, easy to maintain and speeds up the test
development. I have added the comments to explain what the functions do and how they can be used. For
tests as well comments are added to explain the steps of test cases. To avoid flaky tests or false positives I
am using waits in my tests. To interact with elements I used CSS Selectors as it is most efficient way to locate
and interact with the elements.
