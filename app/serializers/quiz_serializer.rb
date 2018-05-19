class QuizSerializer
  include FastJsonapi::ObjectSerializer
  attributes :title, :description
end
