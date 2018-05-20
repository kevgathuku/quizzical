class HomePageController < ApplicationController
  def index
    raw_quizzes = Quiz.all
    @quizzes = QuizSerializer.new(raw_quizzes).serializable_hash
  end
end
