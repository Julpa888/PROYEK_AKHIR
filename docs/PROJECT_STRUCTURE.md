# Project Structure Documentation

## Folder Organization

```
PROYEK_AKHIR/
│
├── src/                          # Main application source code
│   ├── __init__.py              # Package initialization
│   ├── main.py                  # Application core logic
│   ├── autentikasi.py           # Authentication module (login/register)
│   ├── admin_menu.py            # Admin panel features
│   ├── user_menu.py             # User menu features
│   └── storage.py               # Data management (JSON I/O)
│
├── data/                         # Data storage (JSON files)
│   ├── admin.json               # Admin credentials
│   ├── users.json               # User accounts & watchlists
│   └── dramas.json              # Drama database
│
├── tests/                        # Unit tests (for future use)
│   └── README.md                # Testing guidelines
│
├── config/                       # Configuration files (for future use)
│   └── README.md                # Configuration guidelines
│
├── docs/                         # Additional documentation
│   └── ARCHITECTURE.md          # Architecture overview
│
├── main.py                       # Application entry point (at root)
├── requirements.txt              # Python dependencies
├── .gitignore                    # Git ignore file
└── README.md                     # Project documentation
```

## Directory Descriptions

### `/src`
Contains all source code for the application.
- **main.py**: Entry point, handles menu navigation and role-based routing
- **autentikasi.py**: Login/registration system with fallback password handling
- **admin_menu.py**: All admin features (CRUD for dramas, user watchlist viewing)
- **user_menu.py**: User features (watchlist management, drama searching)
- **storage.py**: JSON file handling with path resolution

### `/data`
Stores all application data in JSON format.
- **admin.json**: Admin usernames and passwords
- **users.json**: Regular user accounts with their watchlists
- **dramas.json**: Complete drama database with metadata

### `/tests`
Reserved for unit tests and integration tests.
- Will contain pytest test cases
- Test fixtures and mock data

### `/config`
Reserved for configuration management.
- Environment variables
- Application settings
- Database configuration (for future DB integration)

### `/docs`
Additional documentation and architecture guides.
- Architecture diagrams
- API documentation
- Setup guides

## How to Run

### Simple (Recommended)
```bash
python main.py
```

### From src directory
```bash
cd src
python main.py
```

### With virtual environment
```bash
# Activate venv
.\.venv\Scripts\Activate.ps1

# Run application
python main.py
```

## Import Path Resolution

The `main.py` at root automatically adds `src/` to Python's path, allowing:
- Modules in `src/` to import each other directly
- Data files in `/data` to be found correctly
- Relative paths to work from project root

This design allows running directly from project root without any hassle.

## Benefits of This Structure

✅ **Cleaner Organization**: Separates source code from data and tests
✅ **Scalability**: Easy to add new modules in `src/`
✅ **Testability**: Dedicated `tests/` directory for unit tests
✅ **Maintainability**: Clear separation of concerns
✅ **Professional**: Follows Python project best practices
✅ **Documentation**: Easy to document each section independently

## Future Enhancements

- [ ] Move database to `/data/db` (SQLite or PostgreSQL)
- [ ] Add configuration file in `/config/settings.json`
- [ ] Create unit tests in `/tests/`
- [ ] Add API documentation in `/docs/`
- [ ] Create logging configuration
- [ ] Add database migration scripts

## Notes

- `__pycache__/` and `.pyc` files are automatically generated and ignored by `.gitignore`
- All relative paths in `storage.py` resolve from project root
- The `main.py` file at project root is the entry point
- Source code in `src/` remains modular and reusable
