Rails.application.routes.draw do
  devise_for :users

  scope '/api' do
    resources :quizzes
  end

  namespace :admin do
      resources :quizzes

      root to: "quizzes#index"
    end
  # For details on the DSL available within this file, see http://guides.rubyonrails.org/routing.html
end
