class QuizzesController < ApplicationController
  def index
    @quizzes = Quiz.all
    render json: QuizSerializer.new(@quizzes).serialized_json
  end
end
