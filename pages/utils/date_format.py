from datetime import datetime
import calendar

def _ordinal(n: int) -> str:
    if 10 <= n % 100 <= 20:
        return "th"
    return {1: "st", 2: "nd", 3: "rd"}.get(n % 10, "th")

def _format_time_12(hour: int, minute: int) -> str:
    ampm = "AM" if hour < 12 else "PM"
    h12 = hour % 12
    if h12 == 0:
        h12 = 12
    return f"{h12}:{minute:02d} {ampm}"

def format_timestamp_natural(iso_ts: str) -> str:
    """
    Convierte un timestamp ISO a formato natural en inglés:
    "October 17th of 2025 at 10:30 PM".
    Si no puede parsear, devuelve el string original.
    """
    if not iso_ts:
        return ""
    try:
        date_part, time_part = iso_ts.split("T")
        time_part = time_part.split(".")[0]  # quitar fracciones/zone si existen
        year, month, day = map(int, date_part.split("-"))
        hour, minute, *_ = map(int, time_part.split(":"))
        month_name = calendar.month_name[month]
        return f"{month_name} {day}{_ordinal(day)} of {year} at {_format_time_12(hour, minute)}"
    except Exception:
        # fallback: intentar parseo con datetime por si el formato varía
        try:
            dt = datetime.fromisoformat(iso_ts.replace("Z", ""))
            month_name = calendar.month_name[dt.month]
            return f"{month_name} {dt.day}{_ordinal(dt.day)} of {dt.year} at {_format_time_12(dt.hour, dt.minute)}"
        except Exception:
            return iso_ts