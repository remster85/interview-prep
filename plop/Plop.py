from typing import Optional, Dict
import httpx


def build_bony_sync_http_client(
    *,
    base_url: str,
    cert: Optional[str] = None,  # Or Tuple[str, str] if using cert+key
    proxies: Optional[Dict[str, str]] = None,
    headers: Optional[Dict[str, str]] = None,
    read_timeout: float = 180.0,
    connect_timeout: float = 30.0,
    write_timeout: float = 10.0,
    pool_timeout: float = 10.0,
) -> httpx.Client:
    timeout = httpx.Timeout(
        read=read_timeout,
        connect=connect_timeout,
        write=write_timeout,
        pool=pool_timeout,
    )

    # Optional proxy and cert passed to transport
    transport = httpx.HTTPTransport(
        proxy=proxies.get("https") if proxies else None,
        cert=cert,
        verify=False  # ⚠️ Consider making this configurable
    )

    return httpx.Client(
        base_url=base_url,
        timeout=timeout,
        transport=transport,
        cert=cert,
        headers=headers or {},
    )
