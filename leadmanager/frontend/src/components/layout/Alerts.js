import React, { Component, Fragment } from 'react';
import { connect } from 'react-redux';
import PropTypes from 'prop-types'
import Swal from 'sweetalert2'
 

export class Alerts extends Component {

  static propTypes = {
    error: PropTypes.object.isRequired,
    message: PropTypes.object.isRequired
  }

  showAlert = (title, icon, confirmButtonText='Cool') => {
    Swal.fire({
      title,
      icon,
      confirmButtonText
    })
  }

  componentDidUpdate(prevProps) {
    const { error, alert, message } = this.props;
    if (error !== prevProps.error) {
      if (error.msg.name) this.showAlert(`Name: ${error.msg.name.join()}`, 'error');
      if (error.msg.email) this.showAlert(`Email: ${error.msg.email.join()}`, 'error');
      if (error.msg.message) this.showAlert(`Message: ${error.msg.message.join()}`, 'error');
      if (error.msg.non_field_errors) this.showAlert(`${error.msg.non_field_errors.join()}`, 'error');
      if (error.msg.username) this.showAlert(`${error.msg.username.join()}`, 'error');
    }

    if (message !== prevProps.message) {
      if (message.leadDeleted) this.showAlert(message.leadDeleted, 'success');
      if (message.leadAdded) this.showAlert(message.leadAdded, 'success');
      if (message.passwordNotMatch) this.showAlert(message.passwordNotMatch, 'error');
    }
  }

  render() {
    return (<Fragment />)
  }
}

const mapStateToProps = state => ({
  error: state.errors,
  message: state.messages
});

export default connect(mapStateToProps) (Alerts);