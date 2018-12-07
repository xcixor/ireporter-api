"""Defines the decorators for the error_handlers."""
from flask import Blueprint, make_response, jsonify

ERROR_HANDLERS = Blueprint('error_handlers', __name__)


@ERROR_HANDLERS.errorhandler(404)
def resource_not_found(error):
    """Show custom error for inexisting resource."""
    return jsonify({"error": "Resource not found"}), 404


@ERROR_HANDLERS.errorhandler(500)
def internal_server_error(error):
    """Show custom error for inexisting resource."""
    return jsonify({"error": "Internal Server error"}), 500


@ERROR_HANDLERS.errorhandler(405)
def method_not_allowed(error):
    """Show custom error for inexisting resource."""
    return jsonify({"error": "Internal Server error"}), 405
