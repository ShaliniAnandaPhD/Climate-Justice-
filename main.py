#!/usr/bin/env python3
"""
🔥 GABRIELINO FIRE ASSESSMENT - Main Entry Point 🔥

Multi-agent AI system for fair and efficient insurance claims processing.
"""

import asyncio
import sys
import os

# Add src to path for imports
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

from src.gabrielino_assessment import GabrielinoAssessment
from src.utils.console_utils import console
from config.settings import APP_VERSION


async def main():
    """Main entry point for the Gabrielino Fire Assessment system."""
    try:
        assessment = GabrielinoAssessment()
        
        # Clear screen and show header
        assessment.clear_screen()
        assessment.print_header()
        
        # Show architecture diagram first
        console.print("\n[bold cyan]🏗️ SYSTEM ARCHITECTURE OVERVIEW[/bold cyan]")
        assessment.show_architecture_diagram()
        
        console.print("\n[dim]Press Enter to begin claim intake...[/dim]")
        input()
        
        # Get user input
        assessment.get_user_input()
        
        console.print("\n[dim]Press Enter to start multi-agent analysis...[/dim]")
        input()
        
        # Run the full analysis
        await assessment.run_analysis()
        
        # Final summary
        console.print("\n" + "="*80)
        console.print("[bold green]🎉 GABRIELINO FIRE ASSESSMENT COMPLETE 🎉[/bold green]")
        console.print("="*80)
        console.print("\n[bold]Assessment Summary:[/bold]")
        console.print(f"• Property: [cyan]{assessment.claim_address}[/cyan]")
        console.print(f"• Damage Amount: [yellow]${assessment.claim_damage:,.0f}[/yellow]")
        console.print(f"• Demographic: [magenta]{assessment.claim_demographic.replace('_', ' ').title()}[/magenta]")
        
        console.print("\n[bold]Multi-Agent Benefits Demonstrated:[/bold]")
        console.print("✅ Real-time fire data integration")
        console.print("✅ AI-powered bias detection and mitigation")
        console.print("✅ Historical pattern analysis via local LLM")
        console.print("✅ Parallel processing for sub-second response")
        console.print("✅ Cost-effective alternative to manual review")
        console.print("✅ Comprehensive risk assessment matrix")
        console.print("✅ Actionable recommendations with audit trail")
        
        console.print(f"\n[dim]Thank you for using Gabrielino v{APP_VERSION}! 🔥[/dim]")
        
    except KeyboardInterrupt:
        console.print("\n[yellow]Assessment interrupted by user. Goodbye! 👋[/yellow]")
    except Exception as e:
        console.print(f"\n[bold red]Error: {e}[/bold red]")
        console.print("[dim]Please check your dependencies and configuration.[/dim]")
        import traceback
        console.print(f"[dim]{traceback.format_exc()}[/dim]")


if __name__ == "__main__":
    asyncio.run(main())
