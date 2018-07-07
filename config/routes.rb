Rails.application.routes.draw do
  # API Routes
  namespace :api do
    resources :quizzes
  end

  # React-rendered routes
  root to: "home_page#index"

  namespace :admin do
    resources :quizzes

    root to: "quizzes#index"
  end
end
# For details on the DSL available within this file, see http://guides.rubyonrails.org/routing.html
