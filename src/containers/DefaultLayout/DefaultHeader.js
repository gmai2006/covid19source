import React from 'react';
import { NavLink } from 'react-router-dom';
import { UncontrolledDropdown, Nav, NavItem } from 'reactstrap';
import PropTypes from 'prop-types';

import { AppNavbarBrand, AppSidebarToggler } from '@coreui/react';
import logo from '../../assets/img/brand/logo.svg'
import sygnet from '../../assets/img/brand/sygnet.svg'

const propTypes = {
  children: PropTypes.node,
};



const defaultProps = {};

function DefaultHeader(props) {
  const now = new Date().toString();
    // eslint-disable-next-line
    const { children, ...attributes } = props;

    return (
      <React.Fragment>
        <AppSidebarToggler className="d-lg-none" display="md" mobile />
        <AppNavbarBrand
          full={{ src: logo, width: 200, height: 45, alt: 'DataScience9 Logo' }}
          minimized={{ src: sygnet, width: 30, height: 30, alt: 'DataScience9 Logo' }}
        />
        <AppSidebarToggler className="d-md-down-none" display="lg" />

        <Nav className="d-md-down-none" navbar>
          <NavItem className="px-3">
            <NavLink to="/dashboard" className="nav-link" >CoVid-19 Dashboard</NavLink>
          </NavItem>
       
        </Nav>
        <Nav className="ml-auto" navbar>
        
         
          <UncontrolledDropdown nav direction="down">
            {now}
          </UncontrolledDropdown>
        </Nav>
        
      </React.Fragment>
    );
}

DefaultHeader.propTypes = propTypes;
DefaultHeader.defaultProps = defaultProps;

export default DefaultHeader;
