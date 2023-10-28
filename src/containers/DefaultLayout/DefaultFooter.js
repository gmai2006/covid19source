import React from 'react';

function DefaultFooter(props) {
  // eslint-disable-next-line
  const { children, ...attributes } = props;

  return (
    <React.Fragment>
      <span><a href="https://datascience9.com">DataScience9 LLC</a> &copy; 2019 Datascience9.</span>
    </React.Fragment>
  );
}


export default DefaultFooter;
