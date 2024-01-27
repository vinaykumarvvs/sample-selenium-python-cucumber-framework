Feature: Heroku - Drag And Drop Cases

  @test
  Scenario: Drag A on Top of B
   Given user navigates to HerokuMainPage
   When user on HerokuMainPage clicks on DragAndDrop
   When user on DragAndDropPage drags "A" on top of "B"
   Then user on DragAndDropPage verifies the first block text as "B" and second block text as "A"

  @test
  Scenario: Drag B on Top of A
   Given user navigates to HerokuMainPage
   When user on HerokuMainPage clicks on DragAndDrop
   When user on DragAndDropPage drags "B" on top of "A"
   Then user on DragAndDropPage verifies the first block text as "B" and second block text as "A"