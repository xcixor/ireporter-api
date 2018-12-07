"""Defines the decorators for the error_handlers."""
from flask import Blueprint, make_response, jsonify

error_handlers = Blueprint('error_handlers', __name__)


@error_handlers.errorhandler(404)
def resource_not_found(e):
    """Show custom error for inexisting resource."""
    return jsonify({"error": "Resource not found"}), 404


@error_handlers.errorhandler(500)
def internal_server_error(e):
    """Show custom error for inexisting resource."""
    return jsonify({"error": "Internal Server error"}), 500


@error_handlers.errorhandler(405)
def method_not_allowed(e):
    """Show custom error for inexisting resource."""
    return jsonify({"error": "Internal Server error"}), 405
