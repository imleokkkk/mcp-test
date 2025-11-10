import os
import logging
from fastmcp import FastMCP

# 로깅 설정
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

mcp = FastMCP(name="calculator")

@mcp.tool
def multiply(a: float, b: float) -> float:
    """Multiplies two numbers together."""
    return a * b

if __name__ == "__main__":
    # 환경 변수에서 설정 읽기 (기본값 제공)
    host = os.getenv("HOST", "0.0.0.0")
    port = int(os.getenv("PORT", "8080"))
    
    logger.info(f"Starting MCP server on {host}:{port}")
    
    try:
        mcp.run(transport="http", host=host, port=port)
    except Exception as e:
        logger.error(f"Failed to start server: {e}", exc_info=True)
        raise
