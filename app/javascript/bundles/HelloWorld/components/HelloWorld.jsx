import PropTypes from "prop-types";
import React from "react";

const HelloWorld = props => {
  const { data } = props;

  return (
    <div>
      {data.map(quiz => (
        <React.Fragment key={quiz.id}>
          <h4>{quiz.attributes.title}</h4>
          <p>{quiz.attributes.description}</p>
        </React.Fragment>
      ))}
    </div>
  );
};

HelloWorld.propTypes = {
  data: PropTypes.array.isRequired // this is passed from the Rails view
};

export default HelloWorld;
