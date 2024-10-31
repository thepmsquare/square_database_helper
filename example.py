from square_database_helper import SquareDatabaseHelper

square_database_helper = SquareDatabaseHelper()

# Example: Insert Rows
insert_data = [
    {"test_text": "example"},
]
insert_output = square_database_helper.insert_rows_v0(
    insert_data, "square", "public", "test"
)
print(insert_output)

# Example: Get Rows
get_filters = {}
get_output = square_database_helper.get_rows_v0(
    get_filters, "square", "public", "test", ignore_filters_and_get_all=True, limit=1
)
print(get_output)

# Example: Edit Rows
edit_data = {"test_text": "edited"}
edit_filters = {"test_text": "example"}
edit_output = square_database_helper.edit_rows_v0(
    edit_data, edit_filters, "square", "public", "test"
)
print(edit_output)

# Example: Delete Rows
delete_filters = {"test_text": "edited"}
delete_output = square_database_helper.delete_rows_v0(
    delete_filters, "square", "public", "test"
)
print(delete_output)
