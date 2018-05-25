class HomePageController < ApplicationController
  def index
    @quizzes = Quiz.all
  end
end
