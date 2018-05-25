import PropTypes from "prop-types";
import React from "react";

const HelloWorld = props => {
  const { quizzes } = props;

  return (
    <div>
      {quizzes.map(quiz => (
        <React.Fragment key={quiz.id}>
          <h4>{quiz.title}</h4>
          <p>{quiz.description}</p>
        </React.Fragment>
      ))}
    </div>
  );
};

HelloWorld.propTypes = {
  quizzes: PropTypes.array.isRequired // this is passed from the Rails view
};

export default HelloWorld;
