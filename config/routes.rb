Rails.application.routes.draw do
  namespace :admin do
      resources :quizzes

      root to: "quizzes#index"
    end
  # For details on the DSL available within this file, see http://guides.rubyonrails.org/routing.html
end
